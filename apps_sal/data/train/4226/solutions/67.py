def remove_smallest(numbers=[]):
    a = []
    if numbers == []:
        return []
    for i in numbers:
        a.append(i)
    a.remove(min(a))
    return a

