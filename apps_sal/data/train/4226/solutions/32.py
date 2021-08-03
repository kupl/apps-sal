def remove_smallest(numbers):
    number = numbers[:]

    if number:
        number.remove(min(numbers))
    return number
