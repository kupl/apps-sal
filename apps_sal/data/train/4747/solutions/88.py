def repeat_str(repeat, string):
    result = string
    count = 1
    while count < repeat:
        result += string
        count += 1
    return result
