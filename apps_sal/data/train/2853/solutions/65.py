def solve(arr): 
    ans = []
    for i in arr[::-1]:
        if i not in ans:
            ans = [i]+ans
    return ans
