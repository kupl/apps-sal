T = input()
T = int(T)
for a in range(0, T):
    N = input()
    N = int(N)
    unos = 1
    if N == 1:
        print('INFINITY')
    elif N == 0:
        print(0)
    else:
        for b in range(3, N + 1):
            a = N
            while a >= b:
                a = int(a / b)
                if a == 1:
                    unos += 1
        print(unos)
