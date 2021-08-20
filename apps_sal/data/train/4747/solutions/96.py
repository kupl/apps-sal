def repeat_str(repeat, string):
    output = ''
    count = repeat
    while count > 0:
        output += string
        count -= 1
    return output
