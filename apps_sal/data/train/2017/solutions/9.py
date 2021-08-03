n = int(input())
a = list(map(int, input().split()))
ans = 0
while len(a) > 0:
    if a[0] == a[1]:
        a = a[2:]
        continue
    p = 0
    for i in range(1, len(a)):
        if a[i] == a[0]:
            p = i
            break
    a = a[1:p] + a[p + 1:]
    ans += p - 1
print(ans)
