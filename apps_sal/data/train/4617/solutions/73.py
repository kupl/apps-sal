def powers_of_two(n):
    x = 0
    ans = []
    while x <= n:
        a = 2**x
        x += 1
        ans.append(a)
    return ans
