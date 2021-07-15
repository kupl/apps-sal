def sum_of_minimums(numbers):
    return sum([sorted(numbers[i],reverse=True)[-1] for i in range(len(numbers))])
