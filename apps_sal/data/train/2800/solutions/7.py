from math import *

def find_time_to_break(a,b):
    vShips, netLength = 90/60, 40
    return float('inf') if a==b else netLength/2 / (vShips * sin(radians(abs(b-a)/2)))
