def ones_counter(input):
    (c, result) = (0, [])
    for x in input + [0]:
        if x != 1 and c != 0:
            result.append(c)
            c = 0
        elif x == 1:
            c += 1
    return result
