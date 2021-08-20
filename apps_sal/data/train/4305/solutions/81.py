def order_weight(strng):
    strng_lst = sorted(strng.split())
    weights = [(weight, sum([int(digit) for digit in weight])) for weight in strng_lst]
    sorted_weights = [result[0] for result in sorted(weights, key=lambda result: result[1])]
    return ' '.join(sorted_weights)
