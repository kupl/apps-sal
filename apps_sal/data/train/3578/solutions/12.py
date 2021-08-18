def paperwork(n, m):
    ans = 0

    if n and m > 0:
        ans = n * m

    if ans <= 0:
        ans = 0

    return ans
