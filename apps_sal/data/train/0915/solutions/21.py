T = int(input())
for i in range(0, T):
    N = int(input())
    a = list(map(int, input().strip().split()))[:N]
    lst = []
    count = 0
    for i in a:
        if i in lst:
            pass
        else:
            count = count + 1
            lst.append(i)
    print(count)
