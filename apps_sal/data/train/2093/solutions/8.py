n = int(input())
arr = list(map(int, input().split()))
ans = [0] * 1
ans[0] = []
ans[0].append(arr[0])
for i in range(1, n, 1):
    lo, hi = 0, len(ans)
    idx = -1
    while(lo <= hi):
        mid = (lo + hi) // 2
        # print(lo,hi,i)
        if lo != len(ans) and ans[mid][len(ans[mid]) - 1] < arr[i]:
            idx = mid
            hi = mid - 1
        else:
            lo = mid + 1
    if len(ans) == hi:
        ans.append([])
        ans[hi].append(arr[i])
    else:
        ans[idx].append(arr[i])
for i in range(len(ans)):
    for j in range(len(ans[i])):
        print(ans[i][j], end=" ")
    print()
