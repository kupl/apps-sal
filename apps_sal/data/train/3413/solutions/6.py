def solution(nums):
    if nums == None:
        return []
    if len(nums) < 2:
        return nums
    pivo = nums[0]
    less = [i for i in nums[1:] if i < pivo]
    great = [i for i in nums[1:] if i > pivo]
    return solution(less) + [pivo] + solution(great) 
