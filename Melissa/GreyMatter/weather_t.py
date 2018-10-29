from SenseCells.ptts import ptts
from weather import Weather, Unit

def weather(city_name):
    weather = Weather(unit=Unit.CELSIUS)    #fk farenheit kappa
    location = weather.lookup_by_location('city_name')
    condition = location.condition

    weather_today="The weather is " + str(condition.text) + "with a temperature of" + str(condition.temp) + "degrees celcius in " + city_name
    ptts(weather_today)
