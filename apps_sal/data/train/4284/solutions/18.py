def array_leaders(numbers):
    arr = []
    for i in range(len(numbers) - 1):
        if numbers[i] > sum(numbers[i + 1:]):
            arr.append(numbers[i])
    return arr + [numbers[-1]] if not numbers[-1] <= 0 else arr
