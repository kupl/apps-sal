import math
t = int(input())
for _ in range(t):
    n = int(input())
    s = 0
    a = [int(i) for i in input().split()]
    if n % 2 != 0:
        print("NO")
    else:
        k = n // 2
        f = 0
        for i in range(0, k):
            if a[i] != -1 and a[k + i] != -1:
                if a[i] != a[k + i]:
                    f = 1
                    break
                else:
                    f = 0
        if f == 1:
            print("NO")
        else:
            for i in range(k):
                if a[i] == -1 and a[k + i] == -1:
                    a[i] = 1
                    a[k + i] = 1
                elif a[k + i] == -1:
                    a[k + i] = a[i]
                else:
                    a[i] = a[k + i]
            print("YES")
            for i in range(n):
                print(a[i], end=" ")
            print("")
