def find(nums):
    # hmm, quite fast to use min and max
    return (min(nums) + max(nums)) * (len(nums) + 1) / 2 - sum(nums)
