def sierpinski(n):
    return '\n'.join(l.center(2**(n+1) - 1) for l in addrows(n, ['*']))
    
def addrows(n, t):
    for _ in range(n): t += [l.ljust(len(t[-1])) + " " + l for l in t]        
    return t    
