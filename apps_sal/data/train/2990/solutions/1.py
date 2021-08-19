def monty_hall(c, p):
    print((c, p))
    return round((1 - p.count(c) / len(p)) * 100)
