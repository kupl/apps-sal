t = int(input())
for _ in range(t):
    a, b = input().split()
    d = {}
    for i in range(len(a)):
        try:
            d[a[i]] += [i]
        except:
            d[a[i]] = [i]
    x = list(d.keys())
    x.sort()
    c = -1
    ans = ""
    for i in x:
        if i > b:
            break
        for j in d[i]:
            if j > c:
                c = j
                ans += i

    print(ans + b * (len(a) - len(ans)))
