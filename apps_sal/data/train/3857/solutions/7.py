def lose_weight(gender, weight, duration):
    rate = {'M': 0.015, 'F': 0.012}
    if gender not in ('M', 'F'):
        return 'Invalid gender'
    elif weight <= 0:
        return 'Invalid weight'
    elif duration <= 0:
        return 'Invalid duration'
    else:
        return round(weight * (1 - rate[gender]) ** duration, 1)
