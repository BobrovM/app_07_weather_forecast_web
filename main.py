import streamlit as st
import plotly.express as px
from backend import get_data


st.title("Weather Forecast for the Next Days")

place = st.text_input("Place", value="Marseille")

number_of_days = st.slider("Number of days", 1, 4)

selection = st.selectbox("Data", ("Temperature", "Sky"))

st.header(f"{selection} for the next {number_of_days} days in {place}")

if place:
    data = get_data(place, number_of_days)

    if selection == "Temperature":
        data = [dict["main"]["temp"] for dict in data]
        figure = px.line(x=dates, y=data, labels={"x": "date", "y": "temperature"})
        st.plotly_chart(figure)

    if selection == "Sky":
        data = [dict["weather"][0]["main"] for dict in data]
        st.image()
