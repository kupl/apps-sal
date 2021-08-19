def distinct(seq):
    result = []
    for num in seq:
        if num not in result:
            result.append(num)
    return result
