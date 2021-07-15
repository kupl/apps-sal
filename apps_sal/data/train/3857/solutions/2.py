def lose_weight(gender, weight, duration):
    if gender not in ('M', 'F'):
        return 'Invalid gender'
    if weight <= 0:
        return 'Invalid weight'
    if duration <= 0:
        return 'Invalid duration'
    rate = 0.015 if gender == 'M' else 0.012
    for i in range(duration):
        weight = weight * (1 - rate)
    return float('{:.1f}'.format(weight))
