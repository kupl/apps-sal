def pattern(n):
    h = ''.join(str(i % 10) for i in range(1, n))
    h = h + str(n % 10) * n + h[::-1]
    v = [(str(i % 10) * n).center(len(h)) for i in range(1, n)]
    return '\n'.join(v + [h] * n + v[::-1])
