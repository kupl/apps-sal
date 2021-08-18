for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().strip().split()))
    m = {}
    for i in a:
        if(i not in m):
            m[i] = 1
        else:
            m[i] += 1
    s = set()
    for i in m:
        s.add(m[i])

    if len(s) != len(m):
        print("NO")
        continue
    tt = 1
    for i in range(n):
        flag = 1
        for j in range(i + 1, n):
            if(a[i] != a[j]):
                flag = 0
            if flag == 0 and a[i] == a[j]:
                print("NO")
                tt = 0
                break
        if tt == 0:
            break
    if tt == 1:
        print("YES")
