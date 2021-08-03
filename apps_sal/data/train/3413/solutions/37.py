def solution(nums):
    new_list = []
    while nums:
        min = nums[0]
        for x in nums:
            if x < min:
                min = x
        new_list.append(min)
        nums.remove(min)
    return new_list
