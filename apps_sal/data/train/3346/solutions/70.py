def gap(g, m, n):
    prime = []
    for x in range(m, n):
        if isprime(x):
            if len(prime) == 0:
                prime.append(x)
            else:
                if x - prime[0] == g:
                    return [prime[0], x]
                else:
                    prime[0] = x


def isprime(x):
    if x == 3 or x == 1:
        return True
    elif x % 2 == 0 or x % 3 == 0:
        return False
    i = 5

    while(i * i <= x):
        if x % i == 0 or x % (i + 2) == 0:
            return False
        i += 6
    return True
