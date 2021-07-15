def array_leaders(numbers):
    result, sum = [], 0
    for i in range(len(numbers)):
        if numbers[-i-1] > sum:
            result.insert(0,numbers[-i-1])
        sum += numbers[-i-1]
    return result
