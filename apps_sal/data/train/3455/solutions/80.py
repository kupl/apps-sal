def disarium_number(n):
    return ('Not !!', 'Disarium !!')[sum((int(i) ** a for (a, i) in enumerate(str(n), 1))) == n]
