def bin2gray(bits):
    return [1 - x if i and bits[i - 1] else x for (i, x) in enumerate(bits)]


def gray2bin(bits):
    (result, memo) = ([], bits[0])
    for (i, x) in enumerate(bits):
        if i and x:
            result.append(1 - memo)
        else:
            result.append(memo)
        memo = result[-1]
    return result
