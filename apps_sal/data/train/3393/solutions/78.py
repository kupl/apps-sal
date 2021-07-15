from math import sqrt, pow

def list_divisors(n):
    s = set()
    i = 1
    while i <= sqrt(n):
        if i in s:
            continue
        div, mod = divmod(n, i)
        if (mod == 0) : 
            s.add(i)
            if (div != i): 
                s.add(div)
        i = i + 1
    
    return sorted(list(s))


def list_squared(m, n):
    result = []
    for i in range(m, n + 1):
        divs_sum = sum(pow(d, 2) for d in list_divisors(i))
        if sqrt(divs_sum).is_integer():
            result.append([i, divs_sum])
    return result
        

