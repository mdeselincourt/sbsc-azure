import json, time

import urllib.request
with urllib.request.urlopen("http://api.openweathermap.org/data/2.5/weather?id=2643743&appid=") as response:
    print(str(response))
    weather = json.loads(response.read().decode())
    wind = weather["wind"]
    # print(weather["wind"])

now = time.time()

log=json.loads('{"history":{}}')

log["history"][now]=weather

print(log)