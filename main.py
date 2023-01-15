import streamlit as st
import plotly.express as px
from backend import get_data


st.title("Weather Forecast for the Next Days")

place = st.text_input("Place", value="Marseille")

number_of_days = st.slider("Number of days", 1, 5)

selection = st.selectbox("Data", ("Temperature", "Sky"))

st.header(f"{selection} for the next {number_of_days} days in {place}")

if place:
    data = get_data(place, number_of_days)

    if data == "ERROR":
        selection = ""
        st.info("That place is not registered or does not exist!")

    if selection == "Temperature":
        temperatures = [dict["main"]["temp"]-273.15 for dict in data]
        dates = [dict["dt_txt"] for dict in data]
        figure = px.line(x=dates, y=temperatures, labels={"x": "date", "y": "temperature"})
        st.plotly_chart(figure)

    if selection == "Sky":
        data = [dict["weather"][0]["main"] for dict in data]
        image_paths = {"Clear": "images/clear.png",
                       "Clouds": "images/clouds.png",
                       "Rain": "images/rain.png",
                       "Snow": "images/snow.png"}
        images = [image_paths[condition] for condition in data]
        print(data)
        st.image(images, width=150)
