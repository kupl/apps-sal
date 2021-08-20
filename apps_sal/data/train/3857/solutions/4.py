def lose_weight(gender, weight, duration):
    if gender not in ('M', 'F'):
        return 'Invalid gender'
    if weight <= 0:
        return 'Invalid weight'
    if duration <= 0:
        return 'Invalid duration'
    factor = 0.985 if gender == 'M' else 0.988
    expected_weight = factor ** duration * weight
    return round(expected_weight, 1)
