def remove_smallest(numbers):
    if not numbers:
        return []
    else:
        numbers2 = numbers.copy()
        numbers2.remove(min(numbers2))
        return numbers2

