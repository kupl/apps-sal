def split_the_bill(x):
    m = sum(x.values()) / float(len(x))
    return {k: round(v - m, 2) for (k, v) in x.items()}
