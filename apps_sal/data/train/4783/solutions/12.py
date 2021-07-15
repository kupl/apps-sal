def weather_info (temp):
    celsius = (temp - 32) * (5/9)
    if (celsius > 0):
        return (str(celsius) +  ' is above freezing temperature')
    else:
        return (str(celsius) +  ' is freezing temperature')
    
def convertToCelsius (temperature):
    celsius = (temperature - 32) * (5/9)
    return temperature
