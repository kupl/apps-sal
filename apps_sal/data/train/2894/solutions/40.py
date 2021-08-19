def triple_trouble(one, two, three):
    x = [one, two, three]
    y = max(x, key=len)
    z = len(y)
    a = ''
    for k in range(0, z):
        a += x[0][k] + x[1][k] + x[2][k]
    return a
    # your code here
