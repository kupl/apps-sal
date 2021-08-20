def solution(nums):
    List = []
    if nums != None:
        for num in range(len(nums)):
            minNum = min(nums)
            List.append(minNum)
            nums.remove(minNum)
    return List
