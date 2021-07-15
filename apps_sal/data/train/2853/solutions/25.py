def solve(arr):
    n = len(arr)
    ans = []
    while n > 0:
        if arr[n-1] not in ans:
            ans.append(arr[n-1])
        n -= 1
    return ans[::-1]
