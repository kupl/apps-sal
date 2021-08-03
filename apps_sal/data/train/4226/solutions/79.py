def remove_smallest(numbers):
    copy_numbers = numbers.copy()
    for num in copy_numbers:
        if num <= min(copy_numbers):
            copy_numbers.remove(num)
            break
    return copy_numbers
