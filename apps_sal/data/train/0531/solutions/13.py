n = int(input())
l = []
for i in range(n):
    l.append(list(map(int, (input().split()))))
ans = 0
for i in range(n):
    if i == 0:
        ans += 1
    elif i == n - 1:
        ans += 1
    else:
        if l[i][0] - l[i][1] > l[i - 1][0]:
            ans += 1
        else:
            if l[i][0] + l[i][1] < l[i + 1][0]:
                ans += 1
                l[i][0] = l[i][0] + l[i][1]
print(ans)
