# cook your dish here
for u in range(int(input())):
    n, r = list(map(int, input().split()))
    l = list(map(int, input().split()))
    m = 0
    for i in range(n - 1):
        d = []
        d.append(l[i])
        c = 1
        while(i + c < n):
            d.append(l[i + c])
            d.sort(reverse=True)
            if(d[0] + d[1] <= r):
                c = c + 1
            else:
                break
        if(c > m):
            m = c
    print(m)
