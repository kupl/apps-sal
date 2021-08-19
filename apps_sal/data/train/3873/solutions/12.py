def product_sans_n(nums):
    p = 1
    zeroes = nums.count(0)
    for n in nums:
        if n:
            p *= n
    return [zeroes < 2 and (not n and p if zeroes else p // n) for n in nums]
