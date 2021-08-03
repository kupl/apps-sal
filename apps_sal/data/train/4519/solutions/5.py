def max_number(digits):
    sorted_digits = sorted(str(digits), reverse=True)
    result = ""
    for member in sorted_digits:
        result += str(member)
    return int(result)
