def sum_of_minimums(numbers):
    ms=0
    
    for i in range(len(numbers)):
        ms+=min(numbers[i])
    return ms
