from math import ceil

def cost(minutes):
    return ceil(max(minutes + 25, 90) / 30) * 10

