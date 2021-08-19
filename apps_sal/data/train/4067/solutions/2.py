def iq_test(numbers):
    indexEven = 0
    indexOdd = 0
    numEven = 0
    numOdd = 0
    nums = numbers.split(' ')
    for i in range(len(nums)):
        if int(nums[i]) % 2 == 0:
            numEven += 1
            indexEven = i + 1
        else:
            numOdd += 1
            indexOdd = i + 1
    if numEven == 1:
        return indexEven
    else:
        return indexOdd
