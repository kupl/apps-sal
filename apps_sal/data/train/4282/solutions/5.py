def hungry_seven(arr):
    nums = ''.join((str(a) for a in arr))
    while '789' in nums:
        nums = nums.replace('789', '897')
    return [int(n) for n in nums]
