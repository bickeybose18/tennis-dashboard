import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📈 Analytics")

df = pd.read_csv("Sale Report.csv")

fig = px.pie(df, names="Shipped")
st.plotly_chart(fig)
