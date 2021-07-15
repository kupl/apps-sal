def triple_trouble(one, two, three):
    x = ''
    a = list(one)
    b = list(two)
    c = list(three)
    for i in range(0, max(len(a), len(b), len(c))):
        x = x + a[i] + b[i] + c[i]
    return x
