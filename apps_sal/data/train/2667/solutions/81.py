def zero_fuel(distance, avg, f_l):
    if avg * f_l >= distance:
        return True
    else:
        return False
