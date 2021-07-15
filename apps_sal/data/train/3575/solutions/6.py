def powerset(nums):
    n = len(nums)
    return [[nums[i] for i, item in enumerate(bin(mask)[2:].rjust(n, "0")) if item == "1"] for mask in range(2**n)]

