def two_sum(numbers, target):
    numbers.sort()

    i = 0
    j = len(numbers) - 1

    sum_ = numbers[i] + numbers[j]
    while sum_ != target:
        if sum_ < target:
            i += 1
        elif sum_ > target:
            j -= 1
        sum_ = numbers[i] + numbers[j]
    return [i, j]
