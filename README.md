# 🔐 Email OTP Verification App

A simple and secure Streamlit application for sending and verifying OTPs (One-Time Passwords) via email. Built with Python, this app uses Gmail SMTP and an intuitive web UI to validate email identities.

## 🚀 Features

- 📧 Send 4-digit OTP to any email
- ✅ Verify user-entered OTP in real-time
- 🔒 Environment variable support for credentials
- 🎨 Responsive UI with gradient background
- ☁️ Ready for Streamlit Cloud deployment

## 🖥️ Demo

Live App: [Click here to try]((https://email-otp-verification-app-fjwasepmspwbanprzjhagz.streamlit.app/))
## 📂 Project Structure

email-otp-verification-app/
├── app.py # Main Streamlit app
├── .env.example # Sample environment file (no secrets)
├── requirements.txt # Dependencies
└── README.md # You're here!

bash
Copy code

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/your-username/email-otp-verification-app.git
cd email-otp-verification-app
```

### 2. Create and configure .env

```bash
env
Copy code
EMAIL_USER=your_email@gmail.com
EMAIL_PASS=your_app_password
```

### 3. Install dependencies

```bash
bash
Copy code
pip install -r requirements.txt
```

### 4. Run the app locally

```bash
bash
Copy code
streamlit run app.py
☁️ Deploy to Streamlit Cloud
Push code to GitHub
```

Go to Streamlit Cloud

Click "New App", connect your repo

Set the following secrets under Settings > Secrets:

toml
Copy code
EMAIL_USER="your_email@gmail.com"
EMAIL_PASS="your_app_password"
🛡️ Security Note
Do NOT hardcode credentials in the script.

Always use .env or Streamlit secrets for sensitive information.

🙋‍♀️ Author
Prathyusha Kopur
💼 GitHub | 🌐 LinkedIn

📄 License
This project is licensed under the MIT License.
