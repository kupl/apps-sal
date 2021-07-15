from math import ceil

def growing_plant(up, down, h):
    return max(ceil((h - down) / (up - down)), 1)
