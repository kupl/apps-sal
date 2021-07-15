def sum_of_minimums(numbers):
    mini = []
    for i in range(len(numbers)):
        mini.append(min(numbers[i]))
    return sum(mini)
