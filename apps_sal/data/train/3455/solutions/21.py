def disarium_number(n):
    return ['Not !!', 'Disarium !!'][n == sum((int(b) ** a for (a, b) in enumerate(str(n), 1)))]
