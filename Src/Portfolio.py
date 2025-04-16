import streamlit as st

# 🔧 Page setup
st.set_page_config(
    page_title="Jaideep Kalagara",
    page_icon="👋",
    layout="wide"
)

# 🎯 Intro Header
st.markdown("""
# 👋 Hi, I'm **Jaideep Kalagara**
Welcome to my **personal project portfolio**!  
This is a timeline of my learning journey — some projects are ongoing, some are experiments, and some might be half-finished… and that's okay. 💡
""")

# 🖼️ Profile Image Section
st.image("./Images/portfolio.jpg", width=180, caption="📸 This is me!", use_container_width=False)

# 📌 Sidebar - Quick Bio
st.sidebar.markdown("### 🧑‍💻 About Me")
st.sidebar.success("Hi! I'm Jaideep Kalagara — a passionate builder, problem solver, and educator.")
st.sidebar.markdown("""
**I enjoy:**
- 🧠 Teaching others
- ⚙️ Exploring new technologies
- 🧪 Experimenting with code
- 🐧 Tinkering in Linux
- 🤖 Building robots
""")

# 🗺️ Roadmap Header
st.markdown("## 🛣️ My Learning Journey")

# 🎯 Timeline Blocks — Year-by-Year
roadmap = [
    ("2020", "🧱 The Discovery Phase", [
        "🎮 Saw a cool game on [Roblox](https://www.roblox.com/)",
        "🛠️ Inspired to try building one myself!",
        "🧱 Started with **Scratch** for visual projects",
        "⌨️ No serious coding yet — just creative fun",
        "> _\"I realized I liked building things, even if they were blocks and visuals.\"_"
    ]),
    ("2021", "🚀 First Code Adventures", [
        "🎯 Tried [Unity](https://unity.com/) — didn’t stick, but was fun!",
        "💡 Learned **Lua** and understood it quickly",
        "🧪 Made tiny experiments",
        "🐍 Found **Python** — loved the ecosystem & tutorials",
        "> _\"This was the year I truly stepped into the world of code.\"_"
    ]),
    ("2022–2023", "🤖 Robotic Adventures", [
        "🤖 Joined [VEX Robotics](https://www.vexrobotics.com/)",
        "🧾 Documented code and explained it to teammates",
        "🧑‍🏫 Loved **teaching others** how things worked",
        "🤝 Learned teamwork and real-world coding through robotics"
    ]),
    ("2024", "🧠 Advanced Python & Beyond", [
        "💥 AI started taking off — I followed closely!",
        "💻 Wrote **more advanced Python** projects",
        "🔒 Explored **cybersecurity**",
        "🐧 Switched to Linux",
        "👨‍🏫 Kept teaching and sharing knowledge with friends"
    ]),
    ("2025", "🛠️ Onward", [
        "**🎯 Goals for this year:**",
        "- 👶 Teach younger kids how to code — for free",
        "- 🐍 Level up my Python (especially **backend APIs**)",
        "- 🤖 Continue with robotics projects",
        "- 🧠 Keep improving in **core computer science skills**"
    ])
]

# 🔁 Render roadmap dynamically with consistent formatting
for year, title, items in roadmap:
    col1, col2 = st.columns([1, 3])
    with col1:
        st.markdown(f"### 📅 {year}")
    with col2:
        with st.expander(title):
            for item in items:
                st.markdown(item)

# 🌟 Footer
st.markdown("---")
st.markdown(
    "<center><small>Made with ❤️ using Streamlit · Built by Jaideep Kalagara · Last updated 2025</small></center>",
    unsafe_allow_html=True
)
