def sum_of_minimums(numbers):
    data = []
    for i in range(len(numbers)):
        data.append(min(numbers[i]))

    return (sum(data))
