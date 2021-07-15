from heapq import heappush, heappop
try:
    n, m = list(map(int, input().split()))
    normal = []
    exe = []
    for i in range(0, (n+m)):
        get = int(input())
        if get==-1:
            c = -heappop(normal)
            exe.append(c)
        else:
            heappush(normal, -get)
    for j in exe:
        print(j)
except:
    pass

