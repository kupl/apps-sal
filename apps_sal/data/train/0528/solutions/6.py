t = int(input())
while t:
    t = t - 1
    (N, L) = map(int, input().split())
    if N == 1:
        print(L)
    elif N == 2:
        z = (8 * L + 1) ** 0.5
        z = z - 1
        z = z / 2
        if z - int(z) > 0:
            print(int(z) + 1)
        else:
            print(int(z))
    elif L % N == 0:
        print(L // N)
    else:
        print(1 + L // N)
