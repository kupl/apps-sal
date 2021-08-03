n = int(input())
a = []
f = 0
for i in range(n):
    a.append(list(map(int, input().split())))
for i in range(len(a)):
    for j in range(len(a)):
        if i == j:
            continue
        if i == a[-1]:
            break
        if sum(a[i]) == a[j][0] and sum(a[j]) == a[i][0]:
            f = 1
            break
if f:
    print("YES")
else:
    print("NO")
