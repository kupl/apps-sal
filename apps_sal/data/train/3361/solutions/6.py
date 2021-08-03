def sum_of_minimums(numbers):

    answer = []

    for array in numbers:
        answer.append(min(array))

    return sum(answer)
