for i in range(int(input())):
    n, r, x, y = map(int, input().split())
    if x == 1:
        xli = [int(input())]
    if x > 1:
        xli = list(map(int, input().split()))
    elif x == 0:
        xli = []
    if y > 1:
        yli = list(map(int, input().split()))
    elif y == 1:
        yli = [int(input())]
    elif y == 0:
        yli = []
    ree = n - len(list(set(xli + yli)))
    if ree > r:
        print(r)
    else:
        print(ree)
