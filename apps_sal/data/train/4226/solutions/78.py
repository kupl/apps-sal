def remove_smallest(numbers):
    if numbers:
        numbers_copy = numbers[:]
        smallest_value = numbers_copy[0]
        for i in numbers_copy:
            if i < smallest_value:
                smallest_value = i
        numbers_copy.remove(smallest_value)
        return numbers_copy
    return numbers

