def disarium_number(n):
    s = str(n)
    return 'Disarium !!' if sum([int(y)**(x + 1) for x, y in list(enumerate(s))]) == n else 'Not !!'
