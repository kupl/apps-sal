def disarium_number(n):
    return ['Not !!', 'Disarium !!'][sum((int(y) ** x for (x, y) in enumerate(str(n), 1))) == n]
