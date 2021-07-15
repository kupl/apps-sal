def sum_of_minimums(numbers):
    summ_of_minimums = 0
    for i in range(len(numbers)):
        numbers[i].sort()
        summ_of_minimums += numbers[i][0]
    return(summ_of_minimums)
