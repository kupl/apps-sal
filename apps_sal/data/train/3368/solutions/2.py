def circular_prime(n):
    ns = str(n)
    lp = []
    for i in ns:
        ns = ns[1:] + ns[0]
        lp.append(ns)
    for i in lp:
        for j in range(2, int(i)):
            if int(i) % j == 0:
                return False
    return True and n != 1
