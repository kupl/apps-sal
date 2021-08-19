def find_time_to_break(bearing_A, bearing_B):
    import math
    if bearing_A == bearing_B:
        return float('inf')
    return round(math.sqrt(40 ** 2 / (2 * (1 - math.cos(math.radians(abs(bearing_A - bearing_B)))))) * 2 / 3, 2)
