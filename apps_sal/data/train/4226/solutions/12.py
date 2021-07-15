def remove_smallest(numbers):
    smallest = 0
    for i, num in enumerate(numbers):
        if num < numbers[smallest]:
            smallest = i
    return [x for i, x in enumerate(numbers) if i != smallest]

