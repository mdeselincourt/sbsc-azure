import json, time
import os

apikey = os.environ.get("WEATHER_API_KEY")

import urllib.request
with urllib.request.urlopen("http://api.openweathermap.org/data/2.5/weather?id=2643743&appid={apikey}".format(apikey=apikey)) as response:
    print(str(response))
    weather = json.loads(response.read().decode())
    wind = weather["wind"]
    # print(weather["wind"])

now = time.time()

log=json.loads('{"history":{}}')

log["history"][now]=weather

print(log)