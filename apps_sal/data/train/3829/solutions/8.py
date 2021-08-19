def build_square(blocks):
    nums = {i: blocks.count(i) for i in range(1, 5)}
    odd_comb = min(nums[3], nums[1])
    nums[1] -= odd_comb
    return nums[4] * 4 + odd_comb * 4 + nums[2] * 2 + nums[1] >= 16
