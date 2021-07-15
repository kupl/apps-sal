import math

def calculate_time(battery,charger):
    return math.ceil(battery / charger * 130) / 100
