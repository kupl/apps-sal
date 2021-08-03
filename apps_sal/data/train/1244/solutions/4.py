t = int(input())
c = dict()
k = dict()
for _ in range(t):
    b, d = list(map(int, input().split()))
    if(b not in c):
        c[b] = 1
    else:
        c[b] += 1
    if(d not in k):
        k[d] = 1
    else:
        k[d] += 1
ans = 0
count = 0
p = (10**9) + 7

for i in range(-5 * 100000, 5 * 100000 + 1):
    if(i in c):
        ans = (ans + c[i]) % p
    if(i - 1 in k):
        ans = (ans - k[i - 1]) % p
    count = (count + ans) % p

print(count % (10**9 + 7))
