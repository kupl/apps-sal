from collections import Counter


def find_a_b(nums, target):
    # Edgy edge case 1
    if len(nums) <= 1:
        return None
    # Edgy edge case 2
    if target == 0:
        zeros = nums.count(0)
        if zeros == 0:
            return None
        elif zeros == 1:
            return [0, nums[1]] if nums[0] == 0 else [nums[0], 0]
        else:
            return [nums[0], 0]
    # The main stuff
    counter = Counter(nums)
    for num in nums:
        if num != 0 and target % num == 0:
            complement = target // num
            if ((num == complement and counter[complement] >= 2)
                    or (num != complement and counter[complement] >= 1)):
                return [num, complement]
