def solution(nums):
    print(nums)
    if nums == None:
        return []

    try:
        return sorted(nums)
    except:
        return None
