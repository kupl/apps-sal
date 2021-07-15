from math import factorial as f

def routes(n):
    return f(n * 2) // f(n)**2 if n > 0 else 0
