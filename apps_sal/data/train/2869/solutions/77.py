def distinct(seq):
    result = []
    for num in seq:
        if result.count(num) < 1:
            result.append(num)
    return result
