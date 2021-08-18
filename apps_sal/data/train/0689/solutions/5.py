n = int(input())
a = []
for i in range(n):
    x, y = map(int, input().split())
    a.append([x, x + y])
ans = False
for i in range(n):
    for j in range(n):
        if(i == j):
            continue
        if(a[i][1] == a[j][0] and a[i][0] == a[j][1]):
            ans = True
            break
if(ans):
    print("YES")
else:
    print("NO")
