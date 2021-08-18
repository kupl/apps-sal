def largest_pair_sum(numbers):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(numbers) - 1):
            if numbers[i] > numbers[i + 1]:
                hold_value = numbers[i]
                numbers[i] = numbers[i + 1]
                numbers[i + 1] = hold_value
                swapped = True

    return numbers[-1] + numbers[-2]
