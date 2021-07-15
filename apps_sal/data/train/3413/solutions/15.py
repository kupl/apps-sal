def solution(nums):
    array = []
    try:
        while len(nums) > 0:
            array.append(min(nums))
            nums.remove(min(nums)) 
    except:
        pass
    return array
