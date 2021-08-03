def find_average(nums):
    sum = 0
    for num in nums:
        sum += num

    print(len(nums))
    try:
        avg = sum / len(nums)
    except:
        avg = sum

    return avg
