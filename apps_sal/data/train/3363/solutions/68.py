from itertools import count

def evaporator(content, evap_per_day, threshold):
    percentage = 100
    for day in count(start=1):
        percentage = percentage*(1 - evap_per_day/100)
        if percentage < threshold:
            return day
