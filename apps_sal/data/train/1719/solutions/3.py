def zeroes (base, number):
    fc = get_factor(base)
    return min([find_power(number, i) // fc.count(i) for i in set(fc)])

def get_factor(n):
    li, j = [], 2
    while j * j <= n:
        if n % j : j += 1;continue
        li.append(j)
        n //= j
    if n > 0 : li.append(n)
    return li
    
def find_power(k, b):
    n, c = b, 0
    while k // n:
        c += k // n
        n *= b
    return c
