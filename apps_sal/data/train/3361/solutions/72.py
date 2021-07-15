def sum_of_minimums(numbers):
    accumulator = 0
    for eachlist in numbers:
        accumulator = accumulator + min(eachlist)
    return accumulator
