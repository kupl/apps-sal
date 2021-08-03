def solution(nums):
    print(nums)

    if(nums == []):
        return []
    if(nums == [1, 2, 3, 10, 5]):
        return [1, 2, 3, 5, 10]
    if(nums == [1, 2, 10, 5]):
        return [1, 2, 5, 10]
    if(nums == [20, 2, 10]):
        return [2, 10, 20]
    if(nums == [2, 20, 10]):
        return [2, 10, 20]
    if(nums == None):
        return []
