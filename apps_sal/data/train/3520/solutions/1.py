def prime (number):
    if number < 2: return False
    elif number == 2: return True
    elif number % 2 == 0: return False
    for i in range(3, int(number ** 0.5) + 1, 2):
        if number % i == 0: return False
    return True
    
def step(g, m, n):
    res = []
    i = m
    while (i <= n - g):
        if prime(i) and prime(i + g):
            res.append(i)
            res.append(i + g)
            return res
        i += 1
    return None
