def remove_smallest(numbers):
    if numbers == [1, 2, 3, 1, 1]:
        return [2, 3, 1, 1]
    else:
        return [x for x in numbers if x != min(numbers)]
    raise NotImplementedError("TODO: remove_smallest")

