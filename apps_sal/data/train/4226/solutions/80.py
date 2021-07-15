def remove_smallest(numbers):
    copy_numbers = numbers[:]
    for num in copy_numbers:
        if num <= min(copy_numbers):
            copy_numbers.remove(num)
            return copy_numbers
    return copy_numbers

