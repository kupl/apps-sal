def super_size(n):
    ln = []
    for x in str(n):
        ln.append(x)
    ln.sort()
    ln.reverse()
    return int(''.join(ln))
