for _ in range(int(input())):
    n = int(input())
    c = list(bin(n)[2:])
    for i in range(1, len(c)):
        c[i] = "0"
    c = ''.join(c)
    print(int(c, 2))
