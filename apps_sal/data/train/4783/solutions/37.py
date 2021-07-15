def weather_info (temp):
    if (convert_to_celsius(temp) < 0):
        return f'{convert_to_celsius(temp)} is freezing temperature'
    else:
        return f'{convert_to_celsius(temp)} is above freezing temperature'
    
def convert_to_celsius (temperature):
    celsius = ((temperature) - 32) * (5/9)
    return celsius
weather_info(50)
weather_info(23)
