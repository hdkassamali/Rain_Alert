import requests
from twilio.rest import Client
import config

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = config.api_key

auth_token = config.auth_token
account_sid = config.account_sid
twilio_phone_number = config.twilio_phone_num
my_phone_number = config.my_phone_num



weather_params = {
    "lat": 33.684566,
    "lon": -117.826508,
    "appid": api_key,
    "exclude": "current,daily,minutely",

}

response = requests.get(url=OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain. Remember to bring an ☔️",
        from_=twilio_phone_number,
        to=my_phone_number
    )
    print(message.status)






