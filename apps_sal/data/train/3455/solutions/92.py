true = 'Disarium !!'
false = 'Not !!'


def is_dis(n):
    return sum([int(d) ** i for (i, d) in enumerate(str(n), start=1)]) == n


def disarium_number(n):
    return (false, true)[is_dis(n)]
