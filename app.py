import streamlit as st
import smtplib
import random
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Load credentials securely from Streamlit secrets
EMAIL = st.secrets["EMAIL_ADDRESS"]
PASSWORD = st.secrets["EMAIL_PASSWORD"]

# Page config
st.set_page_config(page_title="Email OTP Verification", page_icon="🔐", layout="centered")

# Background gradient styling
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #FFDEE9 0%, #B5FFFC 100%);
    background-attachment: fixed;
    color: #000000;
}
h1 {
    color: #2C3E50;
    text-align: center;
}
label, input, button {
    font-size: 16px !important;
}
</style>
""", unsafe_allow_html=True)

# Title
st.title("🔐 Email OTP Verification")

# Initialize OTP state
if "otp" not in st.session_state:
    st.session_state.otp = None

# Email Input Form
with st.form("otp_form"):
    user_email = st.text_input("Enter your email address:")
    send_clicked = st.form_submit_button("Send OTP")

    if send_clicked:
        if not user_email.strip():
            st.warning("⚠️ Please enter a valid email address.")
        else:
            st.session_state.otp = random.randint(1111, 9999)
            body = f"Your One-Time Password (OTP) is: {st.session_state.otp}"

            msg = MIMEMultipart()
            msg["From"] = EMAIL
            msg["To"] = user_email
            msg["Subject"] = "OTP for Email Verification"
            msg.attach(MIMEText(body, "plain"))

            try:
                server = smtplib.SMTP("smtp.gmail.com", 587)
                server.starttls()
                server.login(EMAIL, PASSWORD)
                server.send_message(msg)
                server.quit()
                st.success(f"✅ OTP sent successfully to {user_email}")
            except Exception as e:
                st.error(f"❌ Failed to send OTP: {e}")

# OTP Verification
if st.session_state.otp:
    entered_otp = st.text_input("Enter the OTP you received:")
    if st.button("Verify OTP"):
        try:
            if int(entered_otp) == st.session_state.otp:
                st.success("🎉 OTP Verified Successfully!")
                st.session_state.otp = None
            else:
                st.error("❌ Invalid OTP. Please try again.")
        except ValueError:
            st.warning("⚠️ Please enter a valid 4-digit number.")
