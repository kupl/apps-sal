for _ in range(int(input())):
    i = int(input())
    a = str(2**i)
    sums = 0
    for d in a:
        d = int(d)
        sums += d

    print(sums)
