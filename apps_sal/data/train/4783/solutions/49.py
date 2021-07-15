def weather_info (temp):
    c = convert_to_celsius(temp)
    if (c < 0):
        return str(c) + " is freezing temperature"
    else:
        return str(c) + " is above freezing temperature"
    
def convert_to_celsius (temp):
    celsius =float((temp - 32)* (5/9))
    return celsius
