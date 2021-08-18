def find(n):
    ans = 0.0
    for i in range(n + 1):
        if i % 3 == 0 or i % 5 == 0:
            ans += i
    return ans


find(10)
