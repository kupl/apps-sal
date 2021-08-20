import itertools


def nbMonths(my_car, new_car, per_month, loss):
    (loss, w, m) = (1 - loss / 100.0, my_car, 0)
    while w < new_car:
        loss -= 0 if m % 2 == 0 else 0.005
        my_car *= loss
        new_car *= loss
        m += 1
        w = my_car + per_month * m
    return [m, round(w - new_car)]
