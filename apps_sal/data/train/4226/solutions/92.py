def remove_smallest(numbers):
    if numbers == []:
        return []
    else:
        new = numbers.copy()
        least = min(new)
        new.remove(least)
        return new
