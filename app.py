import pickle
import streamlit as st
from scam_detector import detect_scam_indicators


# Load trained ML model and TF-IDF vectorizer
with open("job_scam_model.pkl", "rb") as model_file:
    model = pickle.load(model_file)

with open("tfidf_vectorizer.pkl", "rb") as vectorizer_file:
    vectorizer = pickle.load(vectorizer_file)


# Page configuration
st.set_page_config(
    page_title="AI Job Scam Detection",
    page_icon="🛡️",
    layout="centered"
)


# Title
st.title("🛡️ AI-Powered Job Scam Detection System")
st.write(
    "Analyze a job description or recruitment message "
    "to identify possible scam indicators."
)


# Input
job_text = st.text_area(
    "Paste the job description or recruitment message:",
    height=220,
    placeholder="Paste the job description here..."
)


# Analyze button
if st.button("🔍 Analyze Job"):

    if not job_text.strip():
        st.warning("Please enter a job description or recruitment message.")

    else:
        # ML prediction
        text_vectorized = vectorizer.transform([job_text])
        prediction = model.predict(text_vectorized)[0]

        # Rule-based risk analysis
        indicators, risk_score, risk_level = detect_scam_indicators(job_text)

        st.subheader("Analysis Result")

        if prediction == 1:
            st.error("🚨 ML Prediction: Scam Job")
        else:
            st.success("✅ ML Prediction: Legitimate Job")

        st.write(f"**Risk Score:** {risk_score}/100")
        st.write(f"**Risk Level:** {risk_level}")

        if indicators:
            st.write("### ⚠️ Suspicious Indicators")

            for indicator in indicators:
                st.write(f"- {indicator}")

        else:
            st.success("No common scam indicators found.")