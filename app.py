%%writefile app.py
import streamlit as st
import pandas as pd
import plotly.express as px

st.title("🎬 Film Production Dashboard")

data = {
    "Film": ["Film A", "Film B", "Film C", "Film D", "Film E"],
    "Genre": ["Action", "Drama", "Comedy", "Action", "Horror"],
    "Budget": [100, 150, 80, 120, 60],
    "Revenue": [300, 200, 120, 250, 100]
}

df = pd.DataFrame(data)

st.sidebar.header("Add Film")

film = st.sidebar.text_input("Film Title")
genre = st.sidebar.selectbox("Genre", ["Action", "Drama", "Comedy", "Horror"])
budget = st.sidebar.number_input("Budget", 0)
revenue = st.sidebar.number_input("Revenue", 0)

if st.sidebar.button("Add Film"):
    new_data = pd.DataFrame({
        "Film": [film],
        "Genre": [genre],
        "Budget": [budget],
        "Revenue": [revenue]
    })
    df = pd.concat([df, new_data], ignore_index=True)

df["Profit"] = df["Revenue"] - df["Budget"]
df["ROI"] = df["Profit"] / df["Budget"]

st.subheader("Film Data")
st.dataframe(df)

st.subheader("Budget vs Revenue")
fig = px.bar(df, x="Film", y=["Budget", "Revenue"], barmode="group")
st.plotly_chart(fig)

st.subheader("Genre Distribution")
fig2 = px.pie(df, names="Genre")
st.plotly_chart(fig2)
