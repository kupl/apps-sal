def over_the_road(address, n):
    nums = range(1, 2 * n + 1)
    if address <= n:
        return nums[-address]
    else:
        return nums[2 * n - address]
