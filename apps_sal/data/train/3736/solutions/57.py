def maximum(numbers):
    max_val = numbers[0]
    for i in range(len(numbers)):
        if numbers[i] > max_val:
            max_val = numbers[i]
    return max_val


def minimum(numbers):
    min_val = numbers[0]
    for i in range(len(numbers)):
        if numbers[i] < min_val:
            min_val = numbers[i]
    return min_val
