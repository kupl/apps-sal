def array_leaders(numbers):
    output = []
    for i in range(0, len(numbers) - 1):
        if numbers[i] > sum(numbers[i + 1:]):
            output.append(numbers[i])
    if numbers[-1] > 0:
        output.append(numbers[-1])
    return output
