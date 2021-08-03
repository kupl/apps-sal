def grader(score):
    puntos = float(score)
    if puntos > 1 or puntos < 0.6:
        return 'F'
    elif puntos >= 0.9:
        return 'A'
    elif puntos >= 0.8:
        return 'B'
    elif puntos >= 0.7:
        return 'C'
    elif puntos >= 0.6:
        return 'D'
