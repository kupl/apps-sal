def divisible_by(n, d):
    x = []
    [x.append(i) for i in n if i % d == 0]
    return x
