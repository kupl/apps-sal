for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    pref = []
    # mods = []
    d = {}
    ans = 0
    for i in range(n):
        if i ==0:
            pref.append(a[0])
        else:
            pref.append((pref[-1]+a[i]))
        b = pref[-1]%1000000000
        if b in d.keys():
            if b==0:
                ans +=1
            ans +=d[b]
            d[b]+=1
        else:
            if b==0:
                ans +=1
            d[b] = 1
    print(ans)
