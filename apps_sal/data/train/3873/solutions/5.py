def product_sans_n(nums):
    (zeros, product) = (0, 1)
    for n in nums:
        if n:
            product *= n
        else:
            zeros += 1
    return [zeros < 2 and (not n and product if zeros else product // n) for n in nums]
