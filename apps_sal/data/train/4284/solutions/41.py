def array_leaders(numbers):
    returnlist = []
    for i in range(len(numbers)):
        if numbers[i] > sum(numbers[i + 1:]):
            returnlist.append(numbers[i])
    return returnlist
