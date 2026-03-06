import streamlit as st
import requests

st.set_page_config(page_title="Weather App", layout="centered")

# Your OpenWeatherMap API key
api_key = "979dc16c3da0c2768c45bedf6937985e"

st.title("Live Weather Dashboard")

# List of Indian cities for the dropdown
indian_cities = [
    "Mumbai,IN", "Delhi,IN", "Bengaluru,IN", "Hyderabad,IN", "Ahmedabad,IN",
    "Chennai,IN", "Kolkata,IN", "Pune,IN", "Surat,IN", "Jaipur,IN",
    "Lucknow,IN", "Kanpur,IN", "Nagpur,IN", "Visakhapatnam,IN", "Indore,IN",
    "Thane,IN", "Bhopal,IN", "Patna,IN", "Vadodara,IN", "Ghaziabad,IN",
    "Ludhiana,IN", "Agra,IN", "Nashik,IN", "Faridabad,IN", "Meerut,IN",
    "Rajkot,IN", "Kalyan-Dombivli,IN", "Vasai-Virar,IN", "Varanasi,IN",
    "Srinagar,IN", "Aurangabad,IN", "Dhanbad,IN", "Amritsar,IN",
    "Prayagraj,IN", "Howrah,IN", "Ranchi,IN", "Jabalpur,IN", "Gwalior,IN",
    "Coimbatore,IN", "Vijayawada,IN", "Jodhpur,IN", "Madurai,IN",
    "Raipur,IN", "Kota,IN", "Guwahati,IN", "Chandigarh,IN",
    "Thiruvananthapuram,IN", "Mysuru,IN", "Hubballi-Dharwad,IN",
    "Tiruchirappalli,IN", "Bareilly,IN", "Aligarh,IN", "Moradabad,IN",
    "Bhubaneswar,IN", "Jalandhar,IN", "Bhiwandi,IN", "Tiruppur,IN",
    "Ujjain,IN", "Saharanpur,IN", "Nellore,IN", "Kolhapur,IN",
    "Amravati,IN", "Nagercoil,IN", "Cuttack,IN", "Jammu,IN", "Sangli,IN",
    "Bhavnagar,IN", "Kurnool,IN", "Rohtak,IN", "Hosapete,IN",
    "Shimoga,IN", "Guntur,IN", "Jamnagar,IN", "Warangal,IN",
    "Belagavi,IN", "Mangaluru,IN", "Dehradun,IN"
]

# Create a dropdown for city selection
selected_city = st.selectbox(
    "Select a city:",
    indian_cities
)

if selected_city:
    url = f"http://api.openweathermap.org/data/2.5/weather?q={selected_city}&appid={api_key}&units=metric"

    try:
        response = requests.get(url)
        response.raise_for_status() # Raise an exception for HTTP errors
        weather_data = response.json()

        if weather_data.get("cod") == 200:
            city_name = weather_data['name']
            country = weather_data['sys']['country']
            temperature = weather_data['main']['temp']
            feels_like = weather_data['main']['feels_like']
            description = weather_data['weather'][0]['description']

            st.subheader(f"Current Weather in {city_name}, {country}")
            st.metric(label="Temperature", value=f"{temperature}°C", delta=f"Feels like: {feels_like}°C")
            st.info(f"Description: {description.capitalize()}")
        else:
            st.error(f"Error fetching weather data for {selected_city}: {weather_data.get('message', 'Unknown error')}")
    except requests.exceptions.RequestException as e:
        st.error(f"Network error or invalid response: {e}")
    except Exception as e:
        st.error(f"An unexpected error occurred: {e}")
else:
    st.write("Please select a city to see the weather.")
