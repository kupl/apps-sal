def sum_even_numbers(seq):
    nums = []
    b = 0
    for i in range(len(seq)):
        if seq[i] % 2 == 0:
            nums.append(seq[i])
    for f in range(len(nums)):
        b = b + nums[f]

    return b
