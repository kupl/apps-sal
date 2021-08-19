t = int(input())
while t:
    n = int(input())
    k = 2
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print(k, end='')
            k += 1
        k = i + 2
        print()
    t -= 1
