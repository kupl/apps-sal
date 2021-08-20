def gap(g, m, n):
    (prime, prime1, prime2) = (0, 0, 0)
    for j in range(m, n):
        i = 2
        while i * i <= j:
            if j % i == 0:
                prime = None
                break
            i += 1
        if prime != None:
            if prime1 == 0:
                prime1 = j
            else:
                prime2 = j
        prime = 0
        while prime1 != 0 and prime2 != 0:
            if prime2 - prime1 == g:
                return [prime1, prime2]
            else:
                prime1 = prime2
                break
    return None
