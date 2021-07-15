def weather_info (temp):
    c = convert_to_celsius(temp)
    if (c > 0):
        return str(c) + " is above freezing temperature"
    else:
        return str(c) + " is freezing temperature"
    
def convert_to_celsius (temperature):
  return (temperature - 32) * (5/9)
