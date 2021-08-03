def min_value(digits):
    sorted_digits = sorted(set(digits))
    result = ""
    for member in sorted_digits:
        result += str(member)
    return int(result)
