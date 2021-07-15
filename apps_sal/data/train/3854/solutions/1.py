from itertools import product

def disambiguate(timestamp):
    t = timestamp.split("-")
    return (f"{t[0]}-{t[1+i]}-{t[2-i]}" for i in (0, 1) if (t[1+i] != t[2-i] or i) and t[1+i] < "13")

def check_dates(records):
    result = [0, 0, 0]
    for record in records:
        valid = [list(p) for p in product(*(disambiguate(timestamp) for timestamp in record)) if p[0] <= p[1]]
        result[2 if len(valid) != 1 else 0 if record in valid else 1] += 1
    return result
