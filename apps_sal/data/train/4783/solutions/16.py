def weather_info (temp):
    celsius = (temp - 32) * (5/9)
    if celsius < 0:
        return f"{celsius} is freezing temperature"
    else:
        return f"{celsius} is above freezing temperature"
    
# def convert_to_celsius (temperature):
#    celsius = (temperature) - 32 + (5/9)
#   return celsius

