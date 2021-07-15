def calc_fuel(n):
    n *= 11
    values = {'lava': 800, 'blaze rod': 120, 'coal': 80, 'wood': 15, 'stick': 1}
    usage = {'lava': 0, 'blaze rod': 0, 'coal': 0, 'wood': 0, 'stick': 0}
    
    for fuel_source, duration in list(values.items()):
        if n // duration > 0:
            usage[fuel_source] = n // duration
            n -= n // duration * duration
    
    return usage

