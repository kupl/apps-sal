def square_sum(n):
    return pow(n.pop(0), 2) + square_sum(n) if len(n) > 0 else 0
