def lose_weight(gender, weight, duration):
    if gender not in ('M', 'F'):
        return 'Invalid gender'
    if weight <= 0:
        return 'Invalid weight'
    if duration <= 0:
        return 'Invalid duration'
    return round(weight * (.985 if gender == 'M' else .988) ** round(duration), 1)
