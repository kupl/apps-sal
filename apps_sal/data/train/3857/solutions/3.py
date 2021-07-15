def lose_weight(gender, weight, duration):
    if gender not in "MF":
        return "Invalid gender"
    if weight <= 0:
        return "Invalid weight"
    if duration <= 0:
        return "Invalid duration"
    
    if gender == "M":
        loss = 1 - 1.5 / 100
    else:
        loss = 1 - 1.2 / 100
    
    return round(weight * loss**duration, 1)
