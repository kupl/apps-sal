

t = int(input())

while t:
    n = int(input())

    k = 1
    for i in range(n):
        m = k + i
        for j in range(i + 1):
            print(m - j, end='')
            k += 1

        print()

    t -= 1
