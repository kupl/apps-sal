def split_the_bill(x):
    perperson = 1.0 * sum(x.values()) / len(x)

    for name, val in x.items():
        x[name] = round(val - perperson, 2)

    return x
