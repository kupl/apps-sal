def lose_weight(gender, weight, duration):
    if gender in 'MF':
        if weight > 0:
            if duration > 0:
                for i in range(duration):
                    if gender == 'M':
                        weight -= weight * 0.015
                    else:
                        weight -= weight * 0.012
                return round(weight, 1)
            return 'Invalid duration'
        return 'Invalid weight'
    return 'Invalid gender'
