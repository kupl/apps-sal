def disarium_number(n):
    return 'Disarium !!' if sum(int(x) ** y for y, x in enumerate(str(n), 1)) == n else 'Not !!'
