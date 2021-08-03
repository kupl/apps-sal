arr = []
for _ in range(int(input())):
    start, end = [int(x) for x in input().split()]
    arr.append((start, start + end))
arr.sort()
val = []
for j in range(len(arr) - 1):
    check = arr[j][1]
    ans = 1
    if len(val) > 0 and len(arr) - j > max(val):
        break
    for i in range(1, len(arr)):
        if arr[i][0] > check:
            ans += 1
            check = arr[i][1]
    val.append(ans)
print(max(val))
