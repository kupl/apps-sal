def solution(nums= []):
    if nums == None or len(nums) == 0:
        return [];
    for i in range (len(nums)-1,0,-1):
        # print(i)
        for j in range(i):
            if nums[j] > nums[j+1]:
                helper = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = helper
    return nums
# print(solution(nums))



