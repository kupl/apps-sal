def solve(p):
    (i, ans) = (1, 0)
    while i * i <= p - 1:
        if (p - 1) % i == 0:
            j = (p - 1) // i
            if pow(10, i, p) == 1:
                ans = i
                break
            if pow(10, j, p) == 1:
                ans = j
        i += 1
    if pow(10, ans // 2, p) == p - 1:
        ans = str(ans // 2) + '-altsum'
    else:
        ans = str(ans) + '-sum'
    return ans
