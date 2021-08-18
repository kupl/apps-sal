T = int(input())

for i in range(0, T):
    (x, y) = map(int, input().split())
    z = x + y
    Z = z + 1
    while Z != 0:
        for j in range(2, Z):
            if (Z % j) == 0:
                Z += 1
                break
        else:
            b = Z
            Z = 0
            break
    print(b - z)
