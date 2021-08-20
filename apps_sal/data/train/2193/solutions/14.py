n = int(input())
arrx = []
for i in range(n):
    arr = list(map(int, input().split()))
    arrx.append(sum(arr))
ans = 1
for i in range(1, n):
    if arrx[i] > arrx[0]:
        ans += 1
print(ans)
