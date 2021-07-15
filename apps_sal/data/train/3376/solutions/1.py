def square_free_part(n):

    fac = lambda n: [i for i in range(2, (n//2)+1) if n % i == 0] + [n]
    issquare = lambda n: True if str(n**.5)[-1] == '0' else False
    
    if isinstance(n, bool): return None
    if isinstance(n, int) and n > 0:
        if n == 1: return 1
        if n == 2: return 2
        for i in sorted(fac(n), reverse = True):
            if sum([issquare(f) for f in fac(i)]) == 0: 
                return i
    else: return None
