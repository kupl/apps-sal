def f(n):
    n = n - 1 if n % 2 == 0 else n - 2
    for i in range(n, 1, - 2):
        if len(str(i)) <= sum(1 for j in str(i) if int(j) % 2 == 0) + 1 + int(str(i)[0] == '1'):
            z = True
            for j in range(2, int(i ** 0.5) + 1):
                if i % j == 0:
                    z = False
                    break
            if z:
                return i
