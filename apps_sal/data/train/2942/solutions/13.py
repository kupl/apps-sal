from math import log, ceil

def fold_to(distance, thickness = 0.0001):
    return None if distance < 0 else 0 if distance <= thickness else ceil(log(distance/thickness, 2))
