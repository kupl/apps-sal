def solve(arr):
    ans = []
    arr.reverse()
    for i in arr:
        if i not in ans:
            ans.append(i)
    return ans[::-1]
