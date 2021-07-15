def weather_info (temp):
    c = convertToCelsius(temp)
    return f'{c} {"is freezing temperature" if c<0 else "is above freezing temperature"}'
def convertToCelsius (temperature):
    return (temperature- 32) * (5/9)
