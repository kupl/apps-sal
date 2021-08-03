# cook your dish here
try:
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    x = [-1, -1, -1]
    for i in range(n - 2):
        s = (a[i] + a[i + 1] + a[i + 2]) / 2
        if s > a[i + 2]:
            x[0] = a[i]
            x[1] = a[i + 1]
            x[2] = a[i + 2]
    if x[0] == x[1] == x[2] == -1:
        print("NO")
    else:
        x.sort()
        print("YES")
        print(x[2], x[1], x[0])

except EOFError:
    pass
