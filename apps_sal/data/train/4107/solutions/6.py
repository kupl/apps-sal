from datetime import datetime


def half_life(a, b):
    (a, b) = [datetime.strptime(x, '%Y-%m-%d') for x in (a, b)]
    return (max(a, b) + abs(a - b)).strftime('%Y-%m-%d')
