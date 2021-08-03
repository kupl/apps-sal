def remove_smallest(numbers):
    try:
        smallest = numbers[0]
        for num in numbers:
            if num < smallest:
                smallest = num
    except IndexError:
        return numbers
    else:
        new_numbers = numbers.copy()
        new_numbers.remove(smallest)
        return new_numbers
