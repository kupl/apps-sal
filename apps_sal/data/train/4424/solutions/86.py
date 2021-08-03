def expression_matter(a, b, c):
    x1 = a + b + c
    x2 = (a + b) * c
    x3 = a * (b + c)
    x4 = a * b * c
    nums = []
    nums.append(x1)
    nums.append(x2)
    nums.append(x3)
    nums.append(x4)
    return max(nums)
