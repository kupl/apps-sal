import math

def evaporator(content, evap_per_day, threshold):
    percent_loss = 1 - evap_per_day/100
    x = math.log(threshold/100)/math.log(percent_loss)
    x = math.ceil(x)  
    return x
