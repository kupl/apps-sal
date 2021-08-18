t = int(input())

while t:
    n = int(input())
    k = 1

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print(bin(k)[2:], end=' ')
            k += 1
        print()

    t -= 1
