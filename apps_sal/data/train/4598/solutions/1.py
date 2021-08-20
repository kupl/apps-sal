def calculate(n1, n2, o):

    def s2b(i):
        return int(i, base=2)
    if o == 'add':
        res = s2b(n1) + s2b(n2)
    elif o == 'subtract':
        res = s2b(n1) - s2b(n2)
    elif o == 'multiply':
        res = s2b(n1) * s2b(n2)
    return '{0:b}'.format(res)
