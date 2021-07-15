def weather_info (temp):
    c = convert(temp)
    if c < 0: return "{} is freezing temperature".format(c)
    else: return "{} is above freezing temperature".format(c)
    
def convert(temp):
    return (temp - 32)*(5/9)
