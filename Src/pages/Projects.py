import requests
import streamlit as st

# 🔧 Page config
st.set_page_config(
    page_title="Jaideep Kalagara - My Projects",
    page_icon="📦",
    layout="wide"
)

# 📌 Sidebar
st.sidebar.header("📦 My Projects")
st.sidebar.info("""
Explore some of the cool things I've built or experimented with.
These are fetched live from my GitHub profile.
""")

# 🧠 GitHub API fetcher
def get_repos_with_descriptions(username):
    url = f"https://api.github.com/users/{username}/repos"
    response = requests.get(url)

    if response.status_code == 200:
        repos = response.json()
        return [
            {
                "name": repo["name"],
                "url": repo["html_url"],
                "description": repo["description"] or "_No description provided_",
                "stars": repo["stargazers_count"],
                "language": repo["language"] or "🌐 Unknown",
                "forks": repo["forks_count"]
            }
            for repo in repos
        ]
    else:
        st.error(f"GitHub API error: {response.status_code}")
        return []

# 🗂️ Load repositories
repos = get_repos_with_descriptions("jaideep-kalagara")

# 🧾 Page title
st.markdown("## 🚀 My GitHub Projects")

# 📦 Show each repo in an expander
for repo in repos:
    with st.expander(f"🔗 [{repo['name']}]({repo['url']})"):
        st.markdown(f"**📝 Description:** {repo['description']}")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown(f"🌐 **Language:** `{repo['language']}`")
        with col2:
            st.markdown(f"⭐ **Stars:** {repo['stars']}")
        with col3:
            st.markdown(f"🍴 **Forks:** {repo['forks']}")
