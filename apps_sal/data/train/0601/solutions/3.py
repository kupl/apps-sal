arr = []
for _ in range(int(input())):
    start, end = [int(x) for x in input().split()]
    arr.append((start, start + end))
arr.sort()
ans = 1
check = arr[0][1]
for i in range(1, len(arr)):
    if arr[i][0] > check:
        ans += 1
        check = arr[i][1]
print(ans)
