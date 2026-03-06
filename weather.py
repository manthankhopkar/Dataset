import streamlit as st
import requests

api_key = "979dc16c3da0c2768c45bedf6937985e" # Using the previously defined API key

selected_city = "Pune,IN" # @param ["Mumbai,IN", "Delhi,IN", "Bengaluru,IN", "Hyderabad,IN", "Ahmedabad,IN", "Chennai,IN", "Kolkata,IN", "Pune,IN", "Surat,IN", "Jaipur,IN", "Lucknow,IN", "Kanpur,IN", "Nagpur,IN", "Visakhapatnam,IN", "Indore,IN", "Thane,IN", "Bhopal,IN", "Patna,IN", "Vadodara,IN", "Ghaziabad,IN", "Ludhiana,IN", "Agra,IN", "Nashik,IN", "Faridabad,IN", "Meerut,IN", "Rajkot,IN", "Kalyan-Dombivli,IN", "Vasai-Virar,IN", "Varanasi,IN", "Srinagar,IN", "Aurangabad,IN", "Dhanbad,IN", "Amritsar,IN", "Prayagraj,IN", "Howrah,IN", "Ranchi,IN", "Jabalpur,IN", "Gwalior,IN", "Coimbatore,IN", "Vijayawada,IN", "Jodhpur,IN", "Madurai,IN", "Raipur,IN", "Kota,IN", "Guwahati,IN", "Chandigarh,IN", "Thiruvananthapuram,IN", "Mysuru,IN", "Hubballi-Dharwad,IN", "Tiruchirappalli,IN", "Bareilly,IN", "Aligarh,IN", "Moradabad,IN", "Bhubaneswar,IN", "Jalandhar,IN", "Bhiwandi,IN", "Tiruppur,IN", "Ujjain,IN", "Saharanpur,IN", "Nellore,IN", "Kolhapur,IN", "Amravati,IN", "Nagercoil,IN", "Cuttack,IN", "Jammu,IN", "Sangli,IN", "Bhavnagar,IN", "Kurnool,IN", "Rohtak,IN", "Hosapete,IN", "Shimoga,IN", "Guntur,IN", "Jamnagar,IN", "Warangal,IN", "Belagavi,IN", "Mangaluru,IN", "Dehradun,IN"] {type:"string", label:"Select City"}

url = f"http://api.openweathermap.org/data/2.5/weather?q={selected_city}&appid={api_key}&units=metric"

response = requests.get(url).json()

if response.get("cod") == 200:
    city_name = response['name']
    country = response['sys']['country']
    temperature = response['main']['temp']
    feels_like = response['main']['feels_like']
    description = response['weather'][0]['description']
    print(f"Weather in {city_name}, {country}:")
    print(f"Temperature: {temperature}°C (Feels like: {feels_like}°C)")
    print(f"Description: {description.capitalize()}")
else:
    print(f"Error fetching weather data for {selected_city}: {response.get('message', 'Unknown error')}")
