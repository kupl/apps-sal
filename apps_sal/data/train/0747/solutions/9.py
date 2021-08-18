from collections import defaultdict
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    b = [-1]
    c = [-1]
    prev = nex = 0
    flag = True
    i = 0
    f = False
    while(i < n):
        if flag:
            if a[i] == prev:
                flag = False
                if a[i] == nex:
                    f = True
                    break
                i -= 1
            else:
                b.append(a[i])
                prev = a[i]
        else:
            if a[i] == nex:
                flag = True
                if a[i] == prev:
                    f = True
                    break
                i -= 1
            else:
                c.append(a[i])
                nex = a[i]
        i += 1
    flag = True
    b.sort()
    c.sort(reverse=True)
    ans = b[1:] + c[:-1]
    for i in range(1, len(ans)):
        if ans[i] == ans[i - 1]:
            f = True
            break

    if f:
        print("NO")
    else:
        print("YES")
        for i in ans:
            print(i, end=" ")
        print()
