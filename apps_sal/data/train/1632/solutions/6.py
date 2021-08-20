def countOnes(left, right):

    def f(n):
        c = 0
        a = list(reversed(list(bin(n))))
        for (i, d) in enumerate(a):
            if d == '1':
                c += 1 + 2 ** i * i / 2 + 2 ** i * a[i + 1:].count('1')
        return c
    return f(right) - f(left - 1)
