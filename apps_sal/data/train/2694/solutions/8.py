def paul(a):
    s = sum((5 if x == 'kata' else 10 if x == 'Petes kata' else 1 if x == 'eating' else 0 for x in a))
    return 'Super happy!' if s < 40 else 'Happy!' if s < 70 else 'Sad!' if s < 100 else 'Miserable!'
