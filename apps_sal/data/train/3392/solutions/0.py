def sierpinski(n):
    t = ['*']
    for _ in range(n):
        t = [r.center(2*len(t[-1])+1) for r in t] + [r + ' ' + r for r in t]
    return '\n'.join(t)
