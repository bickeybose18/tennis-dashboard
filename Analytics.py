import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📈 Analytics")

df = pd.read_csv("data/tennis.csv")

fig = px.pie(df, names="Country")
st.plotly_chart(fig)