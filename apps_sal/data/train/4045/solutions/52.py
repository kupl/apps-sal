def number(lines):
    line_number = 1
    formatted = []
    for string in lines:
        formatted.append(str(line_number) + ': ' + string)
        line_number += 1
    return formatted
