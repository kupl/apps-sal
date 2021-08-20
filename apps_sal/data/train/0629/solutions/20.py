for _ in range(int(input())):
    (r, g, b, m) = map(int, input().split())
    Rarr = list(map(int, input().split()))
    Garr = list(map(int, input().split()))
    Barr = list(map(int, input().split()))
    while m > 0:
        Rmax = max(Rarr)
        Gmax = max(Garr)
        Bmax = max(Barr)
        if Rmax == max(Gmax, Rmax, Bmax):
            Rarr = [int(i / 2) for i in Rarr]
        elif Gmax == max(Gmax, Rmax, Bmax):
            Garr = [int(i / 2) for i in Garr]
        else:
            Barr = [int(i / 2) for i in Barr]
        m -= 1
    total = Rarr + Garr + Barr
    total.sort()
    print(total[-1])
