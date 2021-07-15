def remove_smallest(numbers):
    if not numbers:
        return []
    correct_arr = list(numbers)
    correct_arr.remove(min(numbers))
    return correct_arr
