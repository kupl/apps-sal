n = int(input())
l = []
ans = []
i = 1
for p in range(0, n):
    ll = []
    a, b = input().split(" ")
    a = int(a)
    b = int(b)
    ll.append(a)
    ll.append(b)
    l.append(ll)
for j in range(0, len(l)):
    if l[j][0] == 0:
        gcd = l[j][1]
    if l[j][1] == 0:
        gcd = l[j][0]
    if l[j][0] == l[j][1]:
        gcd = l[j][0]
    while(i <= l[j][0] and i <= l[j][1]):
        if(l[j][0] % i == 0 and l[j][1] % i == 0):
            gcd = i
        i = i + 1
    ans.append(gcd)

for k in ans:
    print(k)
