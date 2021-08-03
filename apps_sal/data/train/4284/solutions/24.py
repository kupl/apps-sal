def array_leaders(numbers):
    s = sum(numbers)
    mx = []
    for i in range(len(numbers)):
        if numbers[i] > sum(numbers[i + 1:]):
            mx.append(numbers[i])
    return mx
