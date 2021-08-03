n, k = map(int, input().split())
a = list(map(int, input().split()))

each = sum(a) // k

r = []
s = 0
i = 0
m = 0
while i < n:
    s += a[i]
    m += 1
    if(s == each):
        r.append(m)
        s = 0
        m = 0
    i += 1

if(s == 0 and i == n and m == 0 and len(r) == k):
    print("Yes")
    for i in r:
        print(i, end=" ")
else:
    print("No")
