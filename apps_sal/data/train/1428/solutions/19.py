import heapq
from math import ceil
t = int(input())
for k in range(t):
    (n, a, b, x, y, z) = list(map(int, input().split()))
    c = list(map(int, input().split()))
    cont = [-int(x) for x in c]
    days = int((z - b) / y)
    p_user = days * x + a
    need = z - p_user
    flag = 0
    heapq.heapify(cont)
    count = 0
    if ceil((z - a - 2 * sum(c)) / x) >= days + 1:
        print('RIP')
    elif p_user > z:
        print(0)
    else:
        while p_user < z:
            key = heapq.heappop(cont)
            if key == 0:
                flag = 1
                break
            count += 1
            p_user += -key
            heapq.heappush(cont, int(key / 2))
        if flag == 0:
            print(count)
        else:
            print('RIP')
