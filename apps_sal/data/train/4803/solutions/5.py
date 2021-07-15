def two_sum(numbers, target):
    return [[i, numbers.index(target - numbers[i])] for i in range(len(numbers)) if target - numbers[i] in numbers].pop()
