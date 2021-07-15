def solution(nums):
    arr = []
    while nums:
        minimum = nums[0]
        for i in nums:
            if i < minimum:
                minimum = i
        arr.append(minimum)
        nums.remove(minimum)
    return arr
