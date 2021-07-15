def remove_smallest(numbers):
    if numbers:
        l = [i for i in numbers]
        l.remove(min(l))
        return l
    else:
        return []

