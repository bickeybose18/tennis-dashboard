import streamlit as st
import pandas as pd
import plotly.express as px

st.title(" Dashboard")

df = pd.read_csv("data/tennis.csv")

fig = px.bar(df, x="Player", y="Rank", color="Country")
st.plotly_chart(fig, use_container_width=True)