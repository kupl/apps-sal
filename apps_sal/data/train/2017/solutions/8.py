n = 2 * int(input())
a = [int(i) for i in input().split()]
ans = 0
for i in range(1, len(a), 2):
    j = i
    while a[j] != a[i - 1]:
        j += 1
    while j != i:
        ans += 1
        a[j - 1], a[j] = a[j], a[j - 1]
        j -= 1
print(ans)
