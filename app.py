import streamlit as st
import google.generativeai as genai
import json

# --- PROFESSIONAL UI CONFIG ---
st.set_page_config(page_title="Quizzify-Gen 3", page_icon="🧠", layout="centered")

# --- CUSTOM CSS FOR PORTFOLIO LOOK ---
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stRadio > label { font-weight: bold; color: #1f77b4; }
    div.stButton > button:first-child {
        background-color: #1f77b4; color: white; border-radius: 10px; height: 3em; width: 100%;
    }
    </style>
    """, unsafe_allow_html=True)

# --- API SECURE SETUP ---
api_key = st.secrets.get("GEMINI_API_KEY")

if not api_key:
    st.error("🔑 API Key Missing! Add it to .streamlit/secrets.toml or Streamlit Cloud Secrets.")
    st.stop()

genai.configure(api_key=api_key)

# --- AI LOGIC (GEMINI 3 FLASH) ---
def generate_ai_quiz(topic):
    model = genai.GenerativeModel('gemini-3-flash-preview')
    
    prompt = f"""
    Generate a technical quiz about "{topic}".
    Output MUST be a JSON array of 5 objects. No other text.
    Format:
    [
      {{
        "question": "The question text",
        "options": ["Option A", "Option B", "Option C", "Option D"],
        "answer": "The exact correct option string"
      }}
    ]
    """
    
    try:
        response = model.generate_content(prompt)
        raw_json = response.text.strip().replace("```json", "").replace("```", "")
        return json.loads(raw_json)
    except Exception as e:
        st.error(f"AI Generation Failed: {e}")
        return None

# --- SESSION MANAGEMENT ---
if "questions" not in st.session_state:
    st.session_state.questions = []
if "score_submitted" not in st.session_state:
    st.session_state.score_submitted = False

# --- HEADER ---
st.title("🧠Quizzify-Gen 3")
st.caption("Powered by Gemini 3 Flash")

# --- TOPIC INPUT ---
with st.container():
    col1, col2, col3 = st.columns([3, 1, 1])
    with col1:
        topic = st.text_input("What do you want to be tested on?", placeholder="e.g. Python Loops, Space, etc.")
    with col2:
        st.write("##") # Spacer
        if st.button("AI Generate"):
            if topic:
                with st.spinner("Gemini 3 is thinking..."):
                    data = generate_ai_quiz(topic)
                    if data:
                        st.session_state.questions = data
                        st.session_state.score_submitted = False
                        st.rerun()
            else:
                st.warning("Enter a topic!")
    with col3:
        st.write("##") # Spacer
        if st.button("Static Quiz"):
            # This follows the basic internship requirements strictly
            st.session_state.questions = [
                {"question": "Which keyword is used to define a function in Python?", "options": ["func", "define", "def", "void"], "answer": "def"},
                {"question": "Which data type is immutable in Python?", "options": ["List", "Dictionary", "Set", "Tuple"], "answer": "Tuple"},
                {"question": "What is the correct file extension for Python files?", "options": [".pt", ".py", ".pyt", ".p"], "answer": ".py"},
                {"question": "Which of these is used for multi-line comments in Python?", "options": ["//", "#", "'''", "--"], "answer": "'''"},
                {"question": "What is the output of 2**3 in Python?", "options": ["6", "8", "9", "5"], "answer": "8"}
            ]
            st.session_state.score_submitted = False
            st.rerun()

# --- QUIZ DISPLAY ---
if st.session_state.questions:
    st.divider()
    user_answers = {}
    
    with st.form("quiz_form"):
        for i, q in enumerate(st.session_state.questions):
            st.markdown(f"**Question {i+1}:** {q['question']}")
            
            user_answers[i] = st.radio(
                f"Select answer for Q{i+1}:",
                q['options'],
                index=None,
                key=f"radio_{i}",
                label_visibility="collapsed"
            )
            st.write("") 

        submit_quiz = st.form_submit_button("Finish & Calculate Score")

    # --- RESULT LOGIC ---
    if submit_quiz:
        if None in user_answers.values():
            st.warning("⚠️ Please answer all questions before submitting.")
        else:
            score = 0
            for i, q in enumerate(st.session_state.questions):
                if user_answers[i] == q['answer']:
                    score += 1
            
            st.session_state.score_submitted = True
            
            if score >= 4:
                st.balloons()
                st.success(f"🏆 Outstanding! Score: {score}/5")
            else:
                st.info(f"👍 Good effort! Score: {score}/5")
            
            with st.expander("Review Correct Answers"):
                for q in st.session_state.questions:
                    st.write(f"**Q:** {q['question']}")
                    st.write(f"**A:** :green[{q['answer']}]")
                    st.divider()

# --- FOOTER ---
st.markdown("---")
st.markdown("Designed for **Vertex Development Internship**")