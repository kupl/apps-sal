def find(n):
    l = range(3, n + 1)
    ans = 0
    for i in l:
        if i % 3 == 0 or i % 5 == 0:
            ans += i
    return ans
