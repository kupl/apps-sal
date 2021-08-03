def fun(j, n):
    nonlocal b
    nonlocal g
    active = True
    if b[j] > g[j]:
        for i in range(j, n):
            if g[i] > b[i] or (i > 0 and b[i - 1] > g[i]):
                active = False
                return False
    else:
        for i in range(j, n):
            if g[i] < b[i] or (i > 0 and g[i - 1] > b[i]):
                active = False
                return False
    return True


ls = []
t = int(input())
for z in range(t):
    n = int(input())
    b = list(map(int, input().rstrip().split()))
    g = list(map(int, input().rstrip().split()))
    b.sort()
    g.sort()
    i = 0
    active = True
    while i < n and b[i] == g[i]:
        i += 1
    if i < n:
        active = fun(i, n)
    if active == True:
        ls.append("YES")
    else:
        ls.append("NO")

for i in ls:
    print(i)
