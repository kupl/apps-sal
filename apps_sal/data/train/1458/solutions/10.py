for i in range(int(input())):
    x = int(input())
    c = 0
    for i in range(1, x + 1, 2):
        tot = x - i + 1
        c += tot * tot
    print(c)
