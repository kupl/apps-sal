def cup_volume(d, D, h):
    return round(__import__('math').pi * h / 12 * (d * d + d * D + D * D), 2)
