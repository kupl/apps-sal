def solution(nums):
    r=[]
    while nums:
        mini=min(nums)
        nums.remove(mini)
        r.append(mini)
    return r

