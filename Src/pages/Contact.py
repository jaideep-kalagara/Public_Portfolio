import streamlit as st
import requests
import re


def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None

def notify_telegram(name, email, message):
    token = st.secrets["TELEGRAM_TOKEN"]
    chat_id = st.secrets["TELEGRAM_CHAT_ID"]
    text = f"📩 New message from {name} ({email}):\n{message}"

    url = f"https://api.telegram.org/bot{token}/sendMessage"
    data = {"chat_id": chat_id, "text": text}

    response = requests.post(url, data=data)
    print(response)
    if response.ok:
        st.success("✅ Message sent thanks!")
    else:
        st.error("❌ There was an error sorry!")

# 📄 Page setup
st.set_page_config(
    page_title="Jaideep Kalagara - Contact Me",
    page_icon="📞",
    layout="wide"
)

# 🔗 Sidebar
st.sidebar.header("📬 Get in Touch")
st.sidebar.info("""
If you'd like to connect, feel free to reach out via:
- 📧 Email
- 🌐 GitHub
- 💬 Socials (see below)
""")

# 🧭 Main Header
st.markdown("""
# 📞 Contact Me

Hi! I'm **Jaideep Kalagara** and I'm always open to new ideas, collaborations, or just geeking out over cool tech.  
Feel free to reach out using any of the following platforms 👇
""")

# 📧 Contact Cards
st.markdown("## 📬 Email & Links")

col1, col2 = st.columns(2)
with col1:
    st.markdown("### 📧 Email")
    st.markdown("- kalagarajaideep2013@gmail.com")

    st.markdown("### 🖥️ GitHub")
    st.markdown("- [jaideep-kalagara](https://github.com/jaideep-kalagara)")

# 🧪 Contact form
st.markdown("---")
st.markdown("## 📝 Quick Contact Form")

with st.form("contact_form"):
    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    message = st.text_area("Your Message")

    submitted = st.form_submit_button("Send Message ✉️")

    if submitted:
        if not name or not email or not message:
            st.warning("⚠️ Please fill in all fields before submitting.")
        elif not is_valid_email(email):
            st.warning("⚠️ Please enter a valid email.")
        else:
            notify_telegram(name, email, message)

# 🦶 Footer
st.markdown("---")
st.markdown(
    "<center><small>Designed with ❤️ in Streamlit · © 2025 Jaideep Kalagara</small></center>",
    unsafe_allow_html=True
)
