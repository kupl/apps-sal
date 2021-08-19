def disarium_number(n):
    return 'Disarium !!' if sum([x[1] ** x[0] for x in list(enumerate(list(map(int, list(str(n)))), 1))]) == n else 'Not !!'
