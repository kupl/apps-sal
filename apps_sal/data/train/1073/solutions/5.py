for t in range(0, int(input())):
    z = 1000000007
    ar = [int(i) for i in input().split(" ")]
    if(ar[0] == 1):
        print(ar[1] % z)
    else:
        a = ar[1] % z
        b = ((ar[1] % z) * (ar[1] % z)) % z
        c = (ar[1] - 1) % z
        for i in range(2, ar[0]):
            d = (c * (b + a)) % z
            a = b
            b = d
        print(b)
