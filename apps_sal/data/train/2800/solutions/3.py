def find_time_to_break(bearing_A, bearing_B):
    import math
    # the case we have here will make an isosceles triangle, we just have to solve either half of it.
    bear = abs(bearing_A - bearing_B) / 2
    angle = math.sin(math.radians(bear))
    if angle != 0:
        return round ((20 * 60) / (angle* 90), 2)
    else:
        return float('inf')
