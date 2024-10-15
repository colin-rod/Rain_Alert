import requests
from twilio.rest import Client
import os

API_KEY="4fa5cc8fd4ada961613650e0cb4d9e7e"

#Berlin  lat long
# MY_LAT="52.517427"
# MY_LONG="13.471720"
#Phuket lat long
# MY_LAT = "7.951933"
# MY_LONG = "98.338089"
#Chennai
MY_LAT = "13.082680"
MY_LONG = "80.270721"

account_sid = 'AC445920c1f46d9ea11bfde27ae263a670'
auth_token = '0b6ccc76d3d7cfc43515ec9587fb705d'



parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "APPID": API_KEY,
    "cnt":4
}
response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast",params=parameters)
response.raise_for_status()
weather_data = response.json()
print(weather_data['list'][0]["weather"][0]["id"])


will_rain = False

for hour_data in weather_data['list']:
    condition_code = hour_data['weather'][0]['id']
    if int(condition_code)<700:
        will_rain = True
#weather_ids = [forecast['weather'][0]['id'] for forecast in weather_data['list']]
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        # from_='+19093219816',
        # to='+4915901637965',
        body="It is going to rain today",
        from_ = 'whatsapp:+14155238886',
        to = 'whatsapp:+4915901637965'
    )

    print(message.status)


