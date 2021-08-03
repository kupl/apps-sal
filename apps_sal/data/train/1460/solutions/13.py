n, x, y = list(map(int, input().split()))
a = list(map(int, input().split()))
ans = x * n
temp1 = (y - (y * 2) / 100)
temp2 = (temp1 - (y * 2) / 100)
temp3 = (temp2 - (y * 2) / 100)
temp4 = (temp3 - (y * 2) / 100)
temp5 = (temp4 - (y * 2) / 100)
for i in range(n):
    if a[i] == 1:
        ans += y
    elif a[i] == 2:
        ans += temp1
    elif a[i] == 3:
        ans += temp2
    elif a[i] == 4:
        ans += temp3
    elif a[i] == 5:
        ans += temp4
    elif a[i] == 6:
        ans += temp5
if int(ans) >= 300:
    print("YES")
else:
    print("NO")
