import pyowm

owm = pyowm.OWM('7d1e1ea82891c8bd3e9067781121f41a')

# will it be sunny here this time tomorrow?
forecast = owm.daily_forecast("Exeter,uk")
tomorrow = pyowm.timeutils.tomorrow()
shiny = forecast.will_be_sunny_at(tomorrow)
rainy = forecast.will_be_rainy_at(tomorrow)
stormy = forecast.will_be_stormy_at(tomorrow)
print"Will there be sunshine tomorrow? ", shiny
print"Will it rain tomorrow? ", rainy
print "What about storms? " , stormy

# search for current weather at a place
observation = owm.weather_at_place('Exeter,uk')
w = observation.get_weather()
print w

# weather details
wind = w.get_wind()
humidity = w.get_humidity()
temp = w.get_temperature('celsius')
print "Weather details: Wind ", wind, " Humidity ", humidity, " Temperature ", temp

"""
def listen():
    while True:
        try:
            yield s.receive()
        except scratch.ScratchError:
            raise StopIteration

for msg in listen():
    if 'key' in msg['sensor-update']:
        key = msg['sensor-update']['key']
        owm = pyowm.OWM(key)
    if 'location' in msg['sensor-update']:
        location = msg['sensor-update']['location']
        observation = owm.weather_at_place(location)
        w = observation.get_weather()
        temperature = w.get_temperature()['temp']
        rain = w.get_rain()
        if '1h' in rain:
            rainfall = rain['1h']
        else:
            rainfall = 0
        wind = w.get_wind()
        if 'speed'in wind:
            wind_speed = wind['speed']
        else:
            wind_speed = 0
        if 'deg' in wind:
            wind_direction = wind['deg']
        else:
            wind_direction = 0
        clouds = w.get_clouds()
        s.sensorupdate({'temperature': temperature - 273})
        s.sensorupdate({'rainfall': rainfall})
        s.sensorupdate({'wind_speed': wind_speed})
        s.sensorupdate({'wind_direction': wind_direction})
        s.sensorupdate({'clouds': clouds})
        print ("Location: ",location,"\n","Temp: ",temperature-273,"\n","Rainfall: ",rainfall,"\n","Wind Speed: ",wind_speed,"\n","Wind direction: ",wind_direction,"\n","Clouds: ",clouds)
"""
