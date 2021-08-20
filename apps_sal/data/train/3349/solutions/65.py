def find_missing_number(sequence):
    try:
        nums = list(map(int, sequence.split()))
        nums.sort()
        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i + 1
        return 0
    except:
        return 1
