def split_the_bill(x):
    diff = sum(x.values()) / float(len(x))
    return {k: round(x[k] - diff, 2) for k in x}
