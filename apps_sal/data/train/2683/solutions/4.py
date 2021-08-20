def split_the_bill(group):
    mean = sum(group.values()) / float(len(group))
    return {k: round(v - mean, 2) for (k, v) in group.items()}
