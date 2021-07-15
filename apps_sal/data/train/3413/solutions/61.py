def solution(nums):
    # nums.sort()
    # return nums
    if nums == None:
        return []
    elif len(nums) == 0:
        return []
    for i in range(0, len(nums)):
        print((nums[i]))
        for j in range(0, len(nums)-1):
            print((nums[j]))
            if nums[j] > nums[j+1]:
                temp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = temp

    return nums


