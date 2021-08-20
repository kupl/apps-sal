from collections import Counter as C
p = [2]
for i in range(3, 15000, 2):
    if all((i % j for j in p)):
        p.append(i)


def factors(n):
    a = []
    for i in p:
        while n % i == 0:
            a.append(i)
            n //= i
    if n > 1:
        a.append(n)
    return a


def lcm_cardinality(n):
    if n == 1:
        return 1
    c = list(C(factors(n)).values())
    ans = 0
    for i in range(len(c)):
        m = c[i]
        for j in c[i + 1:]:
            m *= 2 * j + 1
        ans += m
    return ans + 1
