def dot(n,m):
    sep = '+' + '+'.join(['---'] * n) + '+'
    bod = '|' + '|'.join([' o '] * n) + '|'
    def f():
        yield sep
        for i in range(m):
            yield bod
            yield sep
    return '\n'.join(f())
