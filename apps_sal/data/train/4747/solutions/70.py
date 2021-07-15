def repeat_str(repeat, string):
    output = str(string)
    for x in range(repeat-1):
        output += string
    return output
