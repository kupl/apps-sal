(n, k) = map(int, input().split())
a = list(map(int, input().split()))
f = 0
b = []
p = sum(a) // k
q = 0
c = 0
for i in a:
    q += i
    c += 1
    if p == q:
        b.append(c)
        c = 0
        q = 0
    elif q > p:
        f = 1
        break
if f == 1 or len(b) != k or p != sum(a) / k:
    print('No')
else:
    print('Yes')
    for i in b:
        print(i, end=' ')
