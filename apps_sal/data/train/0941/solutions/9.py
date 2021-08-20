def sub(a, b):
    aeven = int(a / 2)
    beven = int(b / 2)
    if a % 2 == 0:
        if b % 2 == 0:
            sum = a * beven
        else:
            sum = b * aeven
    elif b % 2 == 0:
        sum = beven * (aeven + (aeven + 1))
    else:
        sum = beven * aeven + (beven + 1) * (aeven + 1)
    return sum


t = int(input())
for i in range(t):
    (n1, n2) = map(int, input().split(' '))
    print(sub(n1, n2))
