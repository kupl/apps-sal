t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = set(a)
    b = list(b)
    b.sort()
    c = dict()
    for i in range(n):
        if a[i] in c:
            c[a[i]].append(i)
        else:
            c[a[i]] = [i]
    index = -1
    count = 0
    for i in range(len(b)):
        r = c[b[i]]
        flag = 0
        for j in range(len(r)):
            if r[j] > index:
                flag = 1
                index = r[j]
                break
        if flag != 1:
            index = r[0]
            count += 1
    print(count + 1)
