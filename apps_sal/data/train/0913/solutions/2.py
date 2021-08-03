n, m, k = map(int, input().split())
a = []
check = [0] * m
while k != 0:
    x1, y1, x2, y2 = map(int, input().split())
    a.append([x1, y1, x2, y2])
    check[y1 - 1] += 1
    check[y2 - 1] += 1
    k -= 1
maxi = check.index(max(check)) + 1
sum = 0
k = 0
for i in range(len(a)):
    x1, y1, x2, y2 = a[i]
    if y1 != maxi:
        k = abs(y1 - maxi)
        sum += k * 2
    if x1 != x2:
        k = abs(x2 - x1)
        sum += k
    if y2 != maxi:
        k = abs(y2 - maxi)
        sum += k * 2
print(sum)
