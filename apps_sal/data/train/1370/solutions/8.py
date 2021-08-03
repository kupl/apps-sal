t = int(input())
while t:
    n, k = [i for i in input().split()]
    k = len(set(n))
    if k == 3:
        print(27)
    elif k == 2:
        print(8)
    elif k == 1:
        print(1)
    t = t - 1
