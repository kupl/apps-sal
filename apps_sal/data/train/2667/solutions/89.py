def zero_fuel(d, v, g):
    if d <= v * g:
        return True
    else:
        return False
