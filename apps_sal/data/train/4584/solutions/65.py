def invert(lst):
    processed = []
    for number in lst:
        if number < 0:
            processed.append(abs(number))
        else:
            processed.append(number * -1)
    return processed
