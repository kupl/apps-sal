def ff(l, x):
    r = 1
    for i in l:
        if i > x:
            r += 1
    return r


n = int(input())
li = []
r = n * [1]
for i in range(n):
    li.append(int(input()))
    r[i] = ff(li, li[i])
for x in r:
    print(x)
