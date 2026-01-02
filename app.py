import streamlit as st
from agent.agent import Agent

st.set_page_config(page_title="Ambient Authority Confusion Demo", layout="wide")
st.title("Ambient Authority Confusion Demo (Confused Deputy for AI Agents)")

task = st.text_input("Enter your request:", "Summarize today's sales performance")

if st.button("Run Agent"):
    agent = Agent()
    result = agent.run(task)

    st.subheader("Agent Output")
    st.write(result["summary"])

    st.subheader("Agent Reasoning")
    for step in result["reasoning"]:
        st.write("-", step)