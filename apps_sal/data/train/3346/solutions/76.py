def gap(g, m, n):
    last_prime = 2
    for i in range(m, n):
        prime = True

        for j in range(2, int(n**.5)):
            if i % j == 0:
                prime = False
                break

        if prime:
            if i - last_prime == g:
                return [last_prime, i]
            else:
                last_prime = i
