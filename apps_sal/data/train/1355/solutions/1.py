from sys import stdin
for _ in range(int(stdin.readline().strip())) :
    n = int(stdin.readline().strip())
    a = list(map(int,stdin.readline().split()))
    b = []
    for i,ch in enumerate(a) :
        if ch <= n :
            b.append(ch+a[ch-1])
        else :
            while ch >= n :
                ch//=2
            d = n-ch-1
            b.append(a[d])
    print(' '.join(map(str,b)))

