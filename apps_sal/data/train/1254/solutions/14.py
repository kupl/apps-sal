t = int(input())
for i in range(t):
    lst1 = []
    lst1 = [int(item) for item in input().split()]
    N = lst1[0]
    P = lst1[1]
    a = list(map(int, input().strip().split()))[:N]
    e = 0
    d = 0
    for j in a:
        if j >= int(P / 2):
            e = e + 1
        elif j <= int(P / 10):
            d = d + 1
    if e == 1 and d == 2:
        print('yes')
    else:
        print('no')
