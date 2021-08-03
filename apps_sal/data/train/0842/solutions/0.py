t = int(input())
for _ in range(t):
    n = int(input())
    b = 1
    if n % 2:
        c = n - 2
        for j in range(n // 2):
            print(" " * j + str(b) + " " * c + str(b))
            b += 1
            c -= 2
        print(" " * (n // 2) + str(b) + " " * (n // 2))
        b += 1
        c = 1
        for j in range(n // 2):
            print(" " * (n // 2 - j - 1) + str(b) + " " * c + str(b))
            b += 1
            c += 2
    else:
        c = n - 2
        for j in range(n // 2):
            print(" " * j + str(b) + " " * c + str(b))
            b += 1
            c -= 2
        c = 0
        for j in range(n // 2):
            print(" " * (n // 2 - j - 1) + str(b) + " " * c + str(b))
            b += 1
            c += 2
