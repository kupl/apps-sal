import bisect as b
t = int(input())
while(t):
    t -= 1
    n, k = map(int, (input().split()))
    a = list(map(int, input().split()))
    c = 0
    for i in range(n):
        x = [0]
        for j in range(i, n):
            b.insort(x, a[j])
            y = k / (len(x) - 1)
            if(int(y) != y):
                y = int(y) + 1
            y = int(y)
            z = k / y
            if(int(z) != z):
                z = int(z) + 1
            z = int(z)
            q = 1
            l = z - 1
            while(l >= 0):
                if(x[l] != x[z]):
                    break
                q += 1
                l -= 1
            l = z + 1
            # print(x,l)
            while(l < len(x)):
                if(x[l] != x[z]):
                    break
                l += 1
                q += 1
            l = b.bisect(x, q)
            if(x[l - 1] == q):
                c += 1
    print(c)
