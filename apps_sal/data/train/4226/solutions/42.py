def remove_smallest(numbers):
    new_numbers = []
    for number in numbers:
        new_numbers.append(number)
    if len(new_numbers) > 0:
        new_numbers.remove(min(new_numbers))
    return new_numbers
