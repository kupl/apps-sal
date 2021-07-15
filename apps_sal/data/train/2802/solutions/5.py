def per(n):
    ans = []
    while n // 10 > 0:
        acc = 1
        for ch in str(n):
            acc *= int(ch)
        n = acc
        ans.append(n)
    return ans
