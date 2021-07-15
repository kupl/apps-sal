def nth_smallest(arr, pos):
    numbers = arr
    numbers.sort()
    return numbers[pos - 1]
