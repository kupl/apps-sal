from math import sqrt,gcd
def lcm_cardinality(n):
    li = sum([[i] if n // i == i else [i, n // i] for i in range(1, int(sqrt(n))+1) if n % i == 0],[])
    return len([[li[i], li[j]] for i in range(len(li)) for j in range(i, len(li)) if li[i] * li[j]//gcd(li[i], li[j])==n])
