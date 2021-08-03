n = int(input())
arr = list(map(int, input().split()))
cnt_zero, res = 0, 0
for i in range(n - 1, -1, -1):
    if arr[i] == 0:
        cnt_zero += 1
    else:
        res += cnt_zero
print(res)
