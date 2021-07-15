from scipy.constants import golden as φ

def skiponacci(n):
    fib = lambda n: int(round((φ**n - (1-φ)**n) / 5**.5))
    return ' '.join('skip' if n%2 else str(fib(n+1)) for n in range(n))

