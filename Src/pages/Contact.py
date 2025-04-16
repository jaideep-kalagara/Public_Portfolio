import streamlit as st

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
        else:
            subject = f"Portfolio - New Message from {name}"
            body = f"""You received a message from your portfolio site:

Name: {name}
Email: {email}

Message:
{message}
"""
            print(subject, body)
            st.success("Your message has been sent!")

# 🦶 Footer
st.markdown("---")
st.markdown(
    "<center><small>Designed with ❤️ in Streamlit · © 2025 Jaideep Kalagara</small></center>",
    unsafe_allow_html=True
)
