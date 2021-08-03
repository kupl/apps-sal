for _ in range(int(input())):
    a, b = list(map(int, input().split()))
    i = a
    total = 0
    j = 1
    while b > i:
        total = total + a * j
        j += 1
        i += a

    print(total)
