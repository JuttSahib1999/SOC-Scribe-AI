from langchain_community.llms import Ollama
from langchain_core.prompts import PromptTemplate

def get_llm():
    # Using Llama 3 as requested
    return Ollama(model="llama3")

def generate_report_section(raw_data, section_type):
    llm = get_llm()
    
    base_rules = """
    IMPORTANT AI RULES:
    1. Distinguish clearly between confirmed facts, analyst observations, and AI-generated hypotheses.
    2. NEVER fabricate evidence, IPs, hashes, or logs.
    3. Show source event IDs when available.
    4. Align with NIST Incident Response guidance and MITRE ATT&CK where applicable.
    """
    
    prompts = {
        "executive": PromptTemplate.from_template(
            base_rules + "\nGenerate an Executive Summary for this incident including: What happened, When, Affected assets, Business impact, and Current status.\nRaw Data: {data}"
        ),
        "technical": PromptTemplate.from_template(
            base_rules + "\nGenerate a Technical Analysis including: Initial detection, Timeline, IOCs, Attack behavior, Root cause, and MITRE ATT&CK techniques.\nRaw Data: {data}"
        ),
        "response": PromptTemplate.from_template(
            base_rules + "\nGenerate a Response Document detailing: Detection, Investigation, Containment, Eradication, Recovery, and Lessons learned.\nRaw Data: {data}"
        )
    }
    
    if section_type in prompts:
        chain = prompts[section_type] | llm
        return chain.invoke({"data": raw_data})
    return "Invalid section requested."