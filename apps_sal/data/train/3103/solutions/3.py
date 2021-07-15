def unique(integers):
    result = []
    for number in integers:
        if number not in result:
            result.append(number)
    return result
