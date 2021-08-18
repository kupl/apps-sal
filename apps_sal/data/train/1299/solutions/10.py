from collections import Counter
t = int(input())
while(t):
    t -= 1
    n = int(input())
    a = list(map(int, input().split()))
    keys = list(Counter(a).keys())
    l = []
    for i in range(len(keys)):
        ctr = 0
        j = 0
        while(j < n):
            if(keys[i] == a[j]):
                ctr += 1
                j = j + 2
            else:
                j += 1
        l.append(ctr)
    x = max(l)
    ll = []
    for i in range(len(l)):
        if(l[i] == x):
            ll.append(keys[i])
    print(min(ll))
