import streamlit as st
import re
from pipeline import run_research_pipeline

# -------------------------------
# Page Config
# -------------------------------
st.set_page_config(
    page_title="AI Research System",
    page_icon="🤖",
    layout="wide"
)

# -------------------------------
# Styling
# -------------------------------
st.markdown("""
<style>
body {
    background-color: #0f172a;
    color: white;
}
h1, h2, h3 {
    color: #38bdf8;
}
.stButton>button {
    background: linear-gradient(90deg, #6366f1, #22c55e);
    color: white;
    border-radius: 10px;
    height: 3em;
    width: 100%;
    font-size: 18px;
}
</style>
""", unsafe_allow_html=True)

# -------------------------------
# CLEAN TEXT
# -------------------------------
def clean_text(text):
    # Remove code blocks
    text = re.sub(r"```(?:markdown)?", "", text)
    text = text.replace("```", "")

    # Normalize LaTeX
    text = (
        text.replace("\\[", "$$")
            .replace("\\]", "$$")
            .replace("\\(", "$")
            .replace("\\)", "$")
    )

    return text.strip()


# -------------------------------
# FIX TABLES 🔥
# -------------------------------
def fix_tables(text):
    """
    Ensures markdown tables are properly formatted
    """

    lines = text.split("\n")
    new_lines = []
    table_buffer = []

    def flush_table():
        nonlocal table_buffer
        if table_buffer:
            # Ensure separator row exists
            if len(table_buffer) >= 2 and not re.match(r"\|\s*-", table_buffer[1]):
                headers = table_buffer[0].split("|")[1:-1]
                separator = "|" + "|".join([" --- " for _ in headers]) + "|"
                table_buffer.insert(1, separator)

            new_lines.extend(table_buffer)
            table_buffer = []

    for line in lines:
        if "|" in line:
            table_buffer.append(line.strip())
        else:
            flush_table()
            new_lines.append(line)

    flush_table()

    return "\n".join(new_lines)


# -------------------------------
# RENDER FUNCTION
# -------------------------------
def render_content(text):

    text = clean_text(text)
    text = fix_tables(text)

    parts = re.split(r"(\$\$.*?\$\$)", text, flags=re.DOTALL)

    for part in parts:
        part = part.strip()

        if not part:
            continue

        if part.startswith("$$") and part.endswith("$$"):
            st.latex(part[2:-2].strip())
        else:
            st.markdown(part, unsafe_allow_html=True)


# -------------------------------
# UI
# -------------------------------
st.title("🤖 Multi-Agent AI Research System")
st.caption("Search → Analyze → Write → Critique")

topic = st.text_input(
    "🔍 Enter a research topic",
    placeholder="e.g. Attention Is All You Need"
)

if st.button("🚀 Run Research Pipeline"):

    if not topic:
        st.warning("Please enter a topic.")
    else:
        with st.spinner("Running multi-agent system..."):
            result = run_research_pipeline(topic)

        st.success("Research completed!")

        tab1, tab2 = st.tabs(["📄 Report", "🧠 Critic Feedback"])

        with tab1:
            st.markdown("## 📄 Final Report")
            render_content(result["report"])

        with tab2:
            st.markdown("## 🧠 Critic Review")
            render_content(result["feedback"])