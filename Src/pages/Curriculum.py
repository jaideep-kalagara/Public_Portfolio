import streamlit as st

st.set_page_config(
    page_title="Jaideep Kalagara - Python Curriculum",
    page_icon="📘",
    layout="wide"
)

# Sidebar
st.sidebar.header("📘 Python Curriculum")
st.sidebar.info("""
This is the beginner-friendly Python curriculum I’ll be teaching to kids.
It’s designed to be fun, hands-on, and practical!
""")

# Page Header
st.markdown("# 🧑‍🏫 Python Curriculum for Kids")
st.markdown("A structured and playful way to introduce coding with Python.")

# Module 1
with st.expander("🧱 Module 1: Getting Started with Python"):
    st.markdown("""
**Goals:**  
✔️ Understand what Python is  
✔️ Install Python & VS Code  
✔️ Write and run your first script  
✔️ Learn about print statements and basic syntax  
""")

    st.markdown("**Topics Covered:**")
    st.markdown("""
- 📥 Installing Python & Code Editors  
- ✏️ Writing your first line: `print("Hello, world!")`  
- 🧮 Intro to variables and data types  
- 🎨 Using comments and formatting code
""")

# Module 2
with st.expander("🔁 Module 2: Loops & Logic"):
    st.markdown("""
**Goals:**  
✔️ Understand `if` statements  
✔️ Build simple decision-making programs  
✔️ Use loops to repeat actions

**Topics Covered:**
- 🚦 `if`, `else`, and `elif` logic
- 🔁 `for` loops and `while` loops
- 🎲 Building a number guessing game
""")

# Module 3
with st.expander("🎒 Module 3: Lists, Strings, and Functions"):
    st.markdown("""
**Goals:**  
✔️ Learn how to store and manage collections of data  
✔️ Understand how to reuse code with functions

**Topics Covered:**
- 📚 Lists and indexing
- ✂️ String manipulation
- 🧰 Creating and calling functions
- 💬 Mini chatbot with `input()` and `print()`
""")

# Module 4
with st.expander("🎮 Module 4: Mini Projects"):
    st.markdown("""
**Goals:**  
✔️ Apply everything you've learned so far  
✔️ Build fun, interactive projects

**Projects:**
- 🎲 Dice roller simulator  
- 📋 To-do list manager  
- 💬 Chatbot adventure game  
- ⌛ Countdown timer
""")

# Optional Advanced
with st.expander("🚀 Bonus Module: Intro to Turtle Graphics"):
    st.markdown("""
**Goals:**  
✔️ Learn how to draw with code  
✔️ Understand coordinates and functions in action

**Topics Covered:**
- 🐢 Using the `turtle` module
- 🧭 Drawing shapes
- 🎨 Simple artwork and animations
""")

# Footer
st.markdown("---")
st.markdown(
    "<center><small>Designed by Jaideep Kalagara · Teaching with ❤️</small></center>",
    unsafe_allow_html=True
)
