import streamlit as st
import plotly.express as px


def get_data(days):
    dates = ["2022-25-10", "2022-26-10", "2022-27-10"]
    temperatures = [10, 11, 15]
    return dates, temperatures


st.title("Weather Forecast for the Next Days")

place = st.text_input("Place")

number_of_days = st.slider("Number of days", 1, 5)

selection = st.selectbox("Data", ("Temperature", "Sky"))

st.header(f"{selection} for the next {number_of_days} days in {place}")

dates, temperatures = get_data(number_of_days)

figure = px.line(x=dates, y=temperatures, labels={"x": "date", "y": "temperature"})
st.plotly_chart(figure)
