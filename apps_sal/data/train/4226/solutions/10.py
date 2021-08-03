def remove_smallest(numbers):

    empty = []
    z = list(numbers)
    if z == []:
        return empty
    mini = min(z)
    index = numbers.index(mini)
    z.remove(z[index])
    return z
