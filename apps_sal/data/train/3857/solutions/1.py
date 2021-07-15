RATES = {'M': (100-1.5) / 100, 'F': (100-1.2) / 100}

def lose_weight(gender, weight, duration):
    if gender not in RATES:
        return 'Invalid gender'
    if weight <= 0:
        return 'Invalid weight'
    if duration <= 0:
        return 'Invalid duration'
    rate = RATES[gender]
    return round(weight * rate ** duration, 1)
