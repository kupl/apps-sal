def x(n):
    g = []
    for i in range(n // 2 + 1):
        rt = ['□'] * n
        (rt[i], rt[-(i + 1)]) = ('■', '■')
        g.append(rt)
    return '\n'.join((''.join(e) for e in g + g[:-1][::-1]))
