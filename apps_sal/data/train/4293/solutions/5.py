ORM = [('Epley', lambda w, r: w * (1 + r / 30)), ('McGlothin', lambda w, r: 100 * w / (101.3 - 2.67123 * r)), ('Lombardi', lambda w, r: w * r ** 0.1)]


def calculate_1RM(w, r):
    if r == 0:
        return 0
    elif r == 1:
        return w
    else:
        return round(max((func(w, r) for (_, func) in ORM)))
