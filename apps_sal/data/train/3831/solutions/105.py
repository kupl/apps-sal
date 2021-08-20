def angle(n):
    if n > 2:
        ans = 0
        for i in range(n - 2):
            ans = ans + 180
        return ans
