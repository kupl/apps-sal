def number(lines):
    i = 1
    list_lines = []
    for x in lines:
        list_lines.append(f'{i}: {x}')
        i += 1
    return list_lines
