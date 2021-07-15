def remove_smallest(numbers):
    small = numbers[:]
    if small:
        small.remove(min(small))
        return small
    else:
        return numbers

