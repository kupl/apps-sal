import math
t = int(input())
for _ in range(t):
    n = int(input())
    if n == 1:
        print(1)
        continue
    k = math.log(n, 2)
    if k == int(k):
        print(-1)
    else:
        li = [(x + 1) for x in range(n)]
        li[0], li[1], li[2] = 2, 3, 1
        i = 3
        while(i < n):
            if li[i] != 2:
                m = math.log(li[i], 2)
                if m == int(m):
                    li[i], li[i + 1] = li[i + 1], li[i]
                    i += 1
            i += 1
        for i in range(n):
            print(li[i], end=" ")
        print()
