from math import floor


def cockroach_speed(speed_km_per_h: float) -> int:
    """ Get a speed of the cockroach in cm/s based on its speed in km/h. """
    return floor(speed_km_per_h * (100000 / 3600))
