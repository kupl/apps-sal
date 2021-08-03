def distinct(seq):
    result = []
    for item in seq:
        if item not in result:
            result.append(item)

    return result


print(distinct([1, 1, 2]))
