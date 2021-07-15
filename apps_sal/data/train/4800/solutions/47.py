def hotpo(n):
    nums = []
    while n > 1:
        n = 3 * n + 1 if n & 1 else int(n / 2)
        nums.append(n)
    return len(nums)
