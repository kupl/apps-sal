def order(s):
    z = []
    for i in range(1, 10):
        for j in list(s.split()):
            if str(i) in j:
                z.append(j)
    return ' '.join(z)
