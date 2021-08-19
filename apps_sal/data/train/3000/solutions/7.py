def mul_power(n, k):
    z = []
    f = []
    g = []
    for i in range(1, n + 1):
        if n % i == 0:
            z.append(i)
            print(z)
    for c in z:
        f.append(c ** k)
        print(f)
    for j in f:
        g.append(j // n)
        print(g)
    for ele in g:
        if ele * n in f:
            return ele
