def order_weight(strng):
    list2 = strng.split(' ')
    weights = []

    for x in list2:
        digits = list(x)
        for i in range(len(digits)):
            digits[i] = int(digits[i])
        weights.append(sum(digits))

    weights, list2 = zip(*sorted(zip(weights, list2)))
    return str(','.join(list2)).replace(',', ' ')
