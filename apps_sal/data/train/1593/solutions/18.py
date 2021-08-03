t = int(input())

for i in range(t):
    a = int(input())
    notes = [100, 50, 10, 5, 2, 1]
    c = 0
    while a >= 1:
        for i in notes:
            c = c + a // i
            a = a % i

    print(c)
