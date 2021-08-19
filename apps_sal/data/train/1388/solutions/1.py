# cook your dish here
try:
    for _ in range(int(input())):
        x = int(input())
        if x <= 250000:
            print(x)
        elif x <= 500000:
            res = x - ((x - 250000) * (0.05))
            print(int(res))
        elif x <= 750000:
            res = x - (12500 + (x - 500000) * (0.1))
            print(int(res))
        elif x <= 1000000:
            res = x - (12500 + 25000 + (x - 750000) * (0.15))
            print(int(res))
        elif x <= 1250000:
            res = x - (12500 + 25000 + 37500 + (x - 1000000) * (0.2))
            print(int(res))
        elif x <= 1500000:
            res = x - (12500 + 25000 + 37500 + 50000 + (x - 1250000) * (0.25))
            print(int(res))
        else:
            res = x - (12500 + 25000 + 37500 + 50000 + 62500 + (x - 1500000) * (0.3))
            print(int(res))
except:
    pass
