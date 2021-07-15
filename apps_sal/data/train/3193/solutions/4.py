def stairs(n):
    a = [' '.join([str(e)[-1] for e in range(1, i+2)] + [str(i - e + 1)[-1] for e in range(i+1)]) for i in range(n)]
    return '\n'.join(e.rjust(4 * n - 1) for e in a)
