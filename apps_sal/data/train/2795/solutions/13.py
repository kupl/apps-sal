def cockroach_speed(s):
    """
    (number) -> int
    s is the number of kilometers that the cockroach travels per hour. 
    Return the equivalent integer(rounded down) of centimeters per second.
    """
    return int(s * 100000 // 3600)
