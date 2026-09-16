import streamlit as st
import json
import os
from core.database import init_db, Incident
from core.llm_engine import generate_report_section
from core.synthetic_data import get_synthetic_incident
from core.export_utils import export_markdown, export_docx, export_json

st.set_page_config(page_title="SOC-Scribe AI", layout="wide")

st.title("🛡️ SOC-Scribe AI: Incident Report Generator")
st.markdown("Transform raw alerts into NIST/MITRE aligned incident reports locally using Ollama.")

session = init_db()

# Sidebar for Incident Management
with st.sidebar:
    st.header("Incident Management")
    view_mode = st.radio("Navigation", ["Create New Report", "View History"])
    
    if st.button("Load Synthetic SOC Incident"):
        st.session_state['raw_data'] = get_synthetic_incident()
        st.session_state['incident_title'] = "Synthetic Brute Force & RDP Compromise"

if view_mode == "Create New Report":
    title = st.text_input("Incident Title", value=st.session_state.get('incident_title', ''))
    raw_data = st.text_area("Input Raw Data (JSON, CSV, Logs, Analyst Notes)", 
                            height=200, 
                            value=st.session_state.get('raw_data', ''))
    
    if st.button("Generate AI Report"):
        if not raw_data:
            st.error("Please provide raw data to analyze.")
        else:
            with st.spinner("AI is analyzing and writing the Executive Summary..."):
                exec_sum = generate_report_section(raw_data, "executive")
            with st.spinner("AI is mapping MITRE ATT&CK and writing Technical Analysis..."):
                tech_analysis = generate_report_section(raw_data, "technical")
            with st.spinner("AI is structuring NIST Response Steps..."):
                response_act = generate_report_section(raw_data, "response")
            
            # Save to DB
            new_incident = Incident(
                title=title,
                raw_data=raw_data,
                executive_summary=exec_sum,
                technical_analysis=tech_analysis,
                response_actions=response_act
            )
            session.add(new_incident)
            session.commit()
            
            st.session_state['current_incident'] = new_incident.id
            st.success("Report Generated Successfully!")

    # Display current generated report if exists
    if 'current_incident' in st.session_state:
        inc = session.query(Incident).filter_by(id=st.session_state['current_incident']).first()
        if inc:
            st.markdown("---")
            st.subheader("Executive Summary")
            st.write(inc.executive_summary)
            
            st.subheader("Technical Analysis (MITRE Mapped)")
            st.write(inc.technical_analysis)
            
            st.subheader("Response & Remediation (NIST Aligned)")
            st.write(inc.response_actions)
            
            # Export Options
            st.markdown("### Export Report")
            col1, col2, col3 = st.columns(3)
            data_dict = {
                "title": inc.title,
                "executive_summary": inc.executive_summary,
                "technical_analysis": inc.technical_analysis,
                "response_actions": inc.response_actions
            }
            
            with col1:
                md_path = export_markdown(data_dict, "report.md")
                with open(md_path, "r") as f:
                    st.download_button("Download Markdown", f, file_name="report.md")
            with col2:
                docx_path = export_docx(data_dict, "report.docx")
                with open(docx_path, "rb") as f:
                    st.download_button("Download DOCX", f, file_name="report.docx")
            with col3:
                json_path = export_json(data_dict, "report.json")
                with open(json_path, "r") as f:
                    st.download_button("Download JSON", f, file_name="report.json")

elif view_mode == "View History":
    st.header("Previous Incident Reports")
    incidents = session.query(Incident).order_by(Incident.id.desc()).all()
    for inc in incidents:
        with st.expander(f"Incident #{inc.id}: {inc.title}"):
            st.markdown(f"**Status:** {inc.status}")
            st.markdown(f"**Created:** {inc.created_at}")
            st.text_area("Executive Summary", inc.executive_summary, height=150, key=f"es_{inc.id}")