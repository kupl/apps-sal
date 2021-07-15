def array_leaders(numbers):
    return [number for i, number in enumerate(numbers) if numbers[i] > sum(numbers[i+1:len(numbers)])]
