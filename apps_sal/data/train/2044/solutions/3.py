n = list(map(int, input().split(' ')))
a, b = n[0], n[1]
if b >= a - b - 1:
    if a - b == 1:
        print(2)
        for i in range(2, a + 1):
            print(1, i)
    elif a - b == 2:
        print(3)
        print(1, 2)
        print(2, 3)
        for i in range(4, a + 1):
            print(3, i)
    else:
        print(4)
        for i in range(2, a - b + 1):
            print(1, i)
            print(i, i + a - b - 1)
        for i in range(2 * (a - b), a + 1):
            print(a - b, i)
else:
    s = (a - 1) // b
    if (a - 1) % b == 0:
        print(2 * s)
    elif (a - 1) % b == 1:
        print(2 * s + 1)
    else:
        print(2 * s + 2)
    for i in range(1, b + 1):
        print(a, i)
        j = i
        while j + b < a:
            print(j, j + b)
            j = j + b
