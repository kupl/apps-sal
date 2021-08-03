def solution(nums):
    if nums == None:
        return []
    else:
        x = []
        for i in range(len(nums)):
            x.append(min(nums))
            nums.remove(min(nums))
        return x
