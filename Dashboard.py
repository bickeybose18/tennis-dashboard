import streamlit as st
import pandas as pd
import plotly.express as px

# Page config
st.set_page_config(page_title="Tennis Dashboard", layout="wide")

# Title
st.title("🎾 Tennis Analytics Dashboard")

# Load data
df = pd.read_csv("tennis.csv")

# Sidebar filter
st.sidebar.header("🔍 Filters")
country = st.sidebar.selectbox("Select Country", df["Country"].unique())

filtered_df = df[df["Country"] == country]

# Metrics
col1, col2, col3 = st.columns(3)
col1.metric("🏆 Best Rank", int(filtered_df["Rank"].min()))
col2.metric("📊 Avg Rank", round(filtered_df["Rank"].mean(), 2))
col3.metric("👥 Players", filtered_df.shape[0])

# Layout
col1, col2 = st.columns(2)

# Chart
fig = px.bar(filtered_df, x="Rank", y="Player", orientation='h', color="Country")

col1.plotly_chart(fig, use_container_width=True)

# Table
col2.dataframe(filtered_df)
