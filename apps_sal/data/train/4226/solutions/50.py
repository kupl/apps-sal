def remove_smallest(numbers):
    if len(numbers) == 0:
        return []
    else:
        smallest = numbers[0]
    for num in numbers:
        if num < smallest:
            smallest = num
    return [numbers[i] for i in range(len(numbers)) if i != (numbers.index(smallest))]
