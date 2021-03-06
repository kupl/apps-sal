def split_the_bill(x):
    avg = sum(x.values()) / float(len(x))
    group = {}
    for key in x:
        group[key] = round(x[key] - avg, 2)
    return group
