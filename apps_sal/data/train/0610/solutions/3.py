T = int(input())
for i in range(T):
    N = int(input())
    L = list(map(int, input().split()))[:N]
    a, b = [], []
    for j in range(len(L)):
        if L[j] == 1:
            a.append(j)
    for k in range(len(a) - 1):
        b.append(a[k + 1] - a[k])
    for l in range(len(b)):
        if b[l] < 6:
            print("NO")
            break
    else:
        print("YES")
