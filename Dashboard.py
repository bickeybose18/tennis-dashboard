import streamlit as st
import pandas as pd
import plotly.express as px

# Page config
st.set_page_config(page_title="Tennis Dashboard", layout="wide")

# Custom CSS (🔥 Professional look)
st.markdown("""
<style>
.main {
    background-color: #0E1117;
}
h1, h2, h3 {
    color: #FFFFFF;
}
.stMetric {
    background-color: #1E1E2F;
    padding: 15px;
    border-radius: 10px;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

# Title
st.title("🎾 Tennis Analytics Dashboard")
st.markdown("#### Professional Player Insights Dashboard")

# Load data
df = pd.read_csv("tennis.csv")

# Sidebar
st.sidebar.header("🔍 Filters")
country = st.sidebar.selectbox("Select Country", df["Country"].unique())

filtered_df = df[df["Country"] == country]

# KPI Cards
col1, col2, col3 = st.columns(3)

col1.metric("🏆 Best Rank", int(filtered_df["Rank"].min()))
col2.metric("📊 Avg Rank", round(filtered_df["Rank"].mean(), 2))
col3.metric("👥 Players", filtered_df.shape[0])

st.divider()

# Charts Layout
col1, col2 = st.columns([2,1])

# Chart
fig = px.bar(
    filtered_df.sort_values(by="Rank").head(10),
    x="Rank",
    y="Player",
    orientation='h',
    color="Country",
    title="Top 10 Players"
)

col1.plotly_chart(fig, use_container_width=True)

# Table
col2.dataframe(filtered_df.head(10))

st.divider()

# Footer
st.markdown("### 📌 Insights")
st.info("This dashboard shows top tennis player rankings filtered by country.")
