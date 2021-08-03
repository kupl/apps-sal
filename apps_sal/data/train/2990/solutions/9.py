def monty_hall(x, a):
    return round(100 * sum(1 for i in a if i != x) / len(a))
