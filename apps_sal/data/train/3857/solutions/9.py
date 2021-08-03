def lose_weight(gender, weight, duration):
    if gender not in ('M', 'F'):
        return "Invalid gender"
    elif weight <= 0:
        return "Invalid weight"
    elif duration <= 0:
        return "Invalid duration"
    elif gender == 'M':
        return round((weight * (1 - 1.5 / 100) ** duration), 1)
    elif gender == 'F':
        return round((weight * (1 - 1.2 / 100) ** duration), 1)
