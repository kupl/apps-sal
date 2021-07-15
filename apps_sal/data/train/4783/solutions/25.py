def convert_to_celsius (temperature):
    pass
    
def weather_info (celsius):
    celsius = (celsius - 32) * (5/9)
    if (celsius < 0):
        return f"{celsius} is freezing temperature"
    else:
        return f"{celsius} is above freezing temperature"
