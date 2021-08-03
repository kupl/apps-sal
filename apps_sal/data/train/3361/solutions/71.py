def sum_of_minimums(numbers):
    mns = []
    for i in range(len(numbers)):
        mns.append(min(numbers[i]))
    return sum(mns)
