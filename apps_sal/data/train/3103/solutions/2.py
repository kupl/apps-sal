def unique(integers):
    ans = []
    for x in integers:
        if x not in ans:
            ans.append(x)
    return ans
