def similarity(strng1, strng2):
    result = 0
    for c1, c2 in zip(strng1, strng2):
        if c1 != c2:
            break
        result += 1
    return result


def string_suffix(strng):
    return sum(similarity(strng[i:], strng) for i in range(len(strng)))
