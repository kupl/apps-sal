def remove_smallest(numbers):
    numbersCopy = numbers.copy()
    for nums in numbers:
        if nums == min(numbers):
            numbersCopy.remove(nums)
            break
        else:
            None
    return numbersCopy

