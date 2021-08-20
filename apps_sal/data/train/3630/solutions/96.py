def arithmetic(a, b, operator):
    c = ['add', 'subtract', 'multiply', 'divide']
    d = [a + b, a - b, a * b, a / b]
    n = 0
    while c[0] != operator:
        c.remove(c[0])
        n += 1
    return d[n]
