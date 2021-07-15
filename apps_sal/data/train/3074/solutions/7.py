from math import ceil

def growing_plant(up_speed, down_speed, desired_height):
    return max(0, ceil((desired_height - up_speed) / (up_speed - down_speed))) + 1
