import math
for t in range(int(input())):
    n = int(input())
    values = list(map(int, input().split()))
    check = set()
    if n > 60:
        print("NO")
    else:
        for i in range(n):
            check.add(values[i])

        for i in range(n):
            st = 0
            for j in range(i, n):
                st = st | values[j]
                check.add(st)
        d = (n * (n + 1)) // 2
        if len(check) == d:
            print("YES")
        else:
            print("NO")
