def powers_of_two(n):
    p = 0
    ans = []
    while p <= n:
        i = 2 ** p
        p += 1
        ans.append(i)
    return ans
