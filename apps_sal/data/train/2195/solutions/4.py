n = int(input())
arr = list(map(int, input().split()))
arr.sort(reverse=True)
r = 0
s = 0
m = 1
for i in range(1, n):
    if arr[i] < arr[i - 1]:
        s += m
        m = 1
    else:
        m += 1
    if s:
        s -= 1
        r += 1
print(r)

