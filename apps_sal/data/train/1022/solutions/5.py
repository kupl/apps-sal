import math
for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    f = 0
    for i in range(math.ceil(n // 2)):
        if n % 2 == 1:
            f = 1
            break
        else:
            if l[i] != l[i + n // 2]:
                if min(l[i], l[i + n // 2]) == -1:
                    l[i] = max(l[i], l[i + n // 2])
                    l[i + n // 2] = max(l[i], l[i + n // 2])
                else:
                    f = 1
                    break
            else:
                if l[i] == -1:
                    l[i] = 1
                    l[i + n // 2] = 1
    if f == 1:
        print("NO")
    else:
        print("YES")
        print(*l)
