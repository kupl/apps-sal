import math
def step(g, m, n):

    def prime(n):
        if n >= 2:
            for i in range(2, int(math.sqrt(n)) + 1):
                if not (n % i):
                    return False
        else:
            return False
        return True

    for i in range(m,n-g):
        if prime(i + g) and prime(i):
            return [i, i + g]
