from itertools import chain

def pattern(n):
    def f():
        length = 2*n - 1
        lines = [' '] * length
        for i in chain(range(1, n+1), range(n-1, 0, -1)):
            x = str(i % 10)
            lines[i-1] = lines[-i] = x
            yield lines
            lines[i-1] = lines[-i] = ' '
    return '\n'.join(map(''.join, f()))
