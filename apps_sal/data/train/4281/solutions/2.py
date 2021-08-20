import math


def tankvol(h, d, vt):
    r = d / 2
    area_of_liquid = r ** 2 * math.acos(1 - h / r) - (r - h) * (2 * r * h - h * h) ** 0.5
    height_of_cylinder = vt / (math.pi * r * r)
    volume_of_liquid = area_of_liquid * height_of_cylinder
    return math.floor(volume_of_liquid)
