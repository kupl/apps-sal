import operator

def maxl(l, m, mx):
    for i in range(len(l) - 1):
        b1, p1 = l[i]
        if b1 + b1 <= mx:
            break
        for j in range(i + 1, len(l)):
            b2, p2 = l[j]
            if b1 + b2 <= mx:
                break
            if p1 + p2 <= m:
                mx = b1 + b2
                break
    return mx

   
fc = []
fd = []

n, c, d = list(map(int, input().split()))

for _ in range(n):
    b, p, m = input().split()
    b, p = int(b), int(p)
    if m == 'C':
        if p <= c:
            fc.append((b, p))
    else:
        if p <= d:
            fd.append((b, p))

fc.sort(key=operator.itemgetter(0), reverse=True)
fd.sort(key=operator.itemgetter(0), reverse=True)

mx = fc[0][0] + fd[0][0] if fc and fd else 0
mx = maxl(fc, c, mx)
mx = maxl(fd, d, mx)

print(mx)

