# 🧠 Quizzify-Gen 3
> **An Intelligent Dynamic Assessment Engine built for the Vertex Development Internship.**

[![Live App](https://img.shields.io/badge/Live_App-Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://vertex-quiz-platform-gpc3v2se3s639bcbf3u8th.streamlit.app/)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Model: Gemini-3-Flash](https://img.shields.io/badge/AI-Gemini--3--Flash-purple.svg)](https://deepmind.google/technologies/gemini/)

---

## 🌟 The "Internship Plus" Innovation
The original internship task (Task 1) required building a standard quiz platform. While most solutions use a static set of pre-defined questions, I identified a core limitation: **Static quizzes lack scalability and user engagement.**

**My Improvisation:** I upgraded the project into **Vertex Nova-Quiz AI**. By integrating the **Google Gemini 3 Flash LLM**, I transformed a basic script into a dynamic engine that can generate infinite, high-quality technical assessments on any topic a user chooses.

## ✨ Key Features
- **Dynamic AI Generation:** Uses Google's latest **Gemini 3 Flash** model to create unique 5-question quizzes in real-time.
- **Fail-Safe Static Mode:** Includes a robust "Python Basics" mode to ensure 100% uptime and fulfill core internship requirements.
- **Advanced UX Design:** - **Zero-Selection Bias:** Radio buttons are unselected by default (`index=None`), forcing active user recall.
  - **State Management:** Utilizes `st.session_state` to maintain quiz data across user interactions.
- **Professional Analytics:** Instant scoring with visual feedback (balloons/success messages) and a detailed answer-key review.

## 🛠️ Tech Stack
| Component | Technology |
| :--- | :--- |
| **Frontend/UI** | Streamlit (Python-based Web Framework) |
| **AI Backend** | Google Generative AI (Gemini 3 Flash Preview) |
| **Data Handling** | JSON Parsing & Validation |
| **Deployment** | Streamlit Cloud & GitHub |

## 🚀 Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/Hemavarni1501/vertex-quiz-platform.git](https://github.com/Hemavarni1501/vertex-quiz-platform.git)
   cd vertex-quiz-platform
   ```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```
3. **Configure Secrets: Create a .streamlit/secrets.toml file and add your Google API Key:**
 ```bash
GEMINI_API_KEY = "your_api_key_here"
```
4. **Run the App:**
```bash
streamlit run app.py
```
## 👨‍💻 Developed By
### Hemavarni.S Python Programming Intern @ Vertex Development
