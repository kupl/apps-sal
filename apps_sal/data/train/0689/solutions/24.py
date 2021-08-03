a = []
b = []
n = int(input())
for i in range(n):
    c, d = list(map(int, input().split()))
    a.append(c)
    b.append(c + d)
spit = 0

for j in range(0, len(a)):
    for k in range(0, len(b)):
        if a[j] == b[k] and a[k] == b[j]:
            spit = spit + 1
            break

if spit > 0:
    print("YES")
else:
    print("NO")
