def angle(n):
    #your code here
    if n > 2:
        ans = 0
        for i in range(n-2):
            ans = ans + 180
        return ans
