def solution(nums):
    if nums == None:
        return []
    pulls = len(nums)
    if len(nums) == 0:
        return []
    li = []
    for i in range(pulls):
        p = 0
        for n in range(len(nums)):
            if nums[n] < nums[p]:
                p=n
        li.append(nums[p])
        nums = nums[:p] + nums[p+1:]
    return li
