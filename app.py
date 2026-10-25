import streamlit as st
from portfolio_visuals import render_visuals
def research_pipeline(question: str, notes: str) -> dict:
    researcher = {"role": "researcher", "output": notes.strip() or "No evidence notes supplied."}
    analyst = {"role": "analyst", "output": "Evidence supplied: " + ("yes" if notes.strip() else "no")}
    writer = {"role": "writer", "output": f"Question: {question}\n\nDraft based only on supplied notes:\n{researcher['output']}"}
    reviewer = {"role": "reviewer", "output": "Needs source verification before factual claims are treated as verified."}
    return {"steps": [researcher, analyst, writer, reviewer], "report": writer["output"]}

st.set_page_config(page_title="Multi-Agent Research", page_icon="ðŸ§‘â€ðŸ¤â€ðŸ§‘")
render_visuals('05_multi_agent_research')
st.title("Multi-Agent Research Team")
st.caption("Role-based orchestration demo; roles are simulated functions, not separate LLM agents.")
q = st.text_input("Research question")
notes = st.text_area("Evidence notes / source excerpts")
if st.button("Generate report"):
    if not q.strip():
        st.warning("Enter a question.")
    else:
        result = research_pipeline(q, notes)
        st.subheader("Pipeline trace")
        st.json(result["steps"])
        st.subheader("Draft report")
        st.write(result["report"])

