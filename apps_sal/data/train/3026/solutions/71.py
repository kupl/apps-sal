def min_value(digits):
    digits = sorted(list(set(digits)))
    result = ""
    for x in range(len(digits)):
        result += str(digits[x])
    return int(result)
