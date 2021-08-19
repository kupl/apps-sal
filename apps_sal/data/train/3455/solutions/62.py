def disarium_number(number):
    n = list(map(int, str(number)))
    sc = []
    for (i, s) in enumerate(n, 1):
        sc.append(s ** i)
    if sum(sc) == number:
        return 'Disarium !!'
    return 'Not !!'
