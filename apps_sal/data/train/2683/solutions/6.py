def split_the_bill(x):
    avg = 1.0 * sum(x.values()) / len(x)
    return {key: round(value - avg, 2) for key, value in x.items()}
