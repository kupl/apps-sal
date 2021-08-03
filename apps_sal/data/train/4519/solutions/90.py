def max_number(n):
    nums = []
    for elem in str(n):
        nums.append(elem)
    x = "".join(sorted(nums, reverse=True))
    y = int(x)
    return y
