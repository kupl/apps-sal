def solution(nums):
    a = []
    if nums == None:
        return []
    else:
        for x in nums:
            a.append(x)
    a.sort()
    return a
