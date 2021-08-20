def disarium_number(n):
    n = str(n)
    return 'Disarium !!' if sum((int(n[i - 1]) ** i for i in range(1, len(n) + 1))) == int(n) else 'Not !!'
