import streamlit as st
from humanizer import Humanizer

# -----------------------------
# Initialize Humanizer
# -----------------------------
humanizer = Humanizer()

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(
    page_title="HumanizeAI Pro",
    page_icon="✍️",
    layout="wide"
)

# -----------------------------
# Custom CSS
# -----------------------------
st.markdown("""
<style>

/* Main App */
.main{
    padding-top:20px;
}

/* Hide Streamlit Branding */
#MainMenu{
    visibility:hidden;
}

footer{
    visibility:hidden;
}

header{
    visibility:hidden;
}

/* Buttons */
.stButton>button{
    width:100%;
    height:52px;
    border-radius:12px;
    border:none;
    background:#4F46E5;
    color:white;
    font-size:17px;
    font-weight:600;
}

.stButton>button:hover{
    background:#4338CA;
}

/* Text Area */
textarea{
    border-radius:12px !important;
}

/* Metrics */
[data-testid="metric-container"]{
    border-radius:12px;
    padding:15px;
    border:1px solid #E5E7EB;
    box-shadow:0 2px 10px rgba(0,0,0,.05);
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# Title
# -----------------------------
st.title("✍️ HumanizeAI Pro")
st.caption("Transform AI-generated text into natural human writing.")

# -----------------------------
# Session State
# -----------------------------
if "output" not in st.session_state:
    st.session_state.output = ""

if "stats" not in st.session_state:
    st.session_state.stats = {
        "words": 0,
        "characters": 0,
        "reading_time": "0 min",
        "quality": "--"
    }

# -----------------------------
# Layout
# -----------------------------
col1, col2 = st.columns(2)

# -----------------------------
# Input Column
# -----------------------------
with col1:

    st.subheader("Input")

    style = st.selectbox(
        "Writing Style",
        [
            "Academic",
            "Assignment",
            "Research Paper",
            "Professional",
            "Casual"
        ]
    )

    input_text = st.text_area(
        "Paste AI-generated text",
        height=350,
        placeholder="Paste your AI-generated content here..."
    )

    if st.button("✨ Humanize Text", use_container_width=True):

        output_text, info = humanizer.humanize(
            input_text,
            style
        )

        st.session_state.output = output_text

        reading_time = max(1, round(info["words"] / 200))

        st.session_state.stats = {
            "words": info["words"],
            "characters": info["characters"],
            "reading_time": f"{reading_time} min",
            "quality": "Good"
        }

# -----------------------------
# Output Column
# -----------------------------
with col2:

    st.subheader("Humanized Output")

    st.text_area(
        "",
        value=st.session_state.output,
        height=350
    )

    # Copy Box
    st.code(
        st.session_state.output,
        language=None
    )

# -----------------------------
# Statistics
# -----------------------------
st.divider()

c1, c2, c3, c4 = st.columns(4)

c1.metric(
    "Words",
    st.session_state.stats["words"]
)

c2.metric(
    "Characters",
    st.session_state.stats["characters"]
)

c3.metric(
    "Reading Time",
    st.session_state.stats["reading_time"]
)

c4.metric(
    "Quality",
    st.session_state.stats["quality"]
)
