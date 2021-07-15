def remove_smallest(numbers):
    if numbers == []:
        return []
    else:
        res = []
        for i in numbers:
            res.append(i)
        res.remove(min(numbers))
        return res
