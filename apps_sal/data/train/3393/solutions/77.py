from math import *
def list_squared(m, n):
    def factors(x):
        lst = []
        for i in range(1, int(sqrt(x) + 1)):
            if x % i == 0:
                lst.append(i)
                if x != i ** 2:
                    lst.append(x / i)
        return sum([k ** 2 for k in lst])
    return [[j, factors(j)] for j in range(m, n + 1) if sqrt(factors(j)) % 1 == 0]      
