def split_the_bill(d):
    avg = sum(d.values()) / len(d)
    return {n: round(v - avg, 2) for n, v in d.items()}
