def solve(arr):
    arrr = arr[::-1]
    ans = []
    for i in arrr:
        if i not in ans:
            ans.append(i)
    return ans[::-1]
