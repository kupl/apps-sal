def lose_weight(gender, weight, duration):
    if not gender in ['M', 'F']:
        return 'Invalid gender'
    if weight <= 0:
        return 'Invalid weight'
    if duration <= 0:
        return 'Invalid duration'
    nl = 0.985 if gender == 'M' else 0.988
    for i in range(duration):
        weight *= nl
    return round(weight, 1)
