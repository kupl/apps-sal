def number(lines):
    new_list = []
    index = 0
    new_el = 1
    while len(lines) != index:
        el = lines[index]
        sum_el = f'{new_el}: {el}'
        new_list.append(sum_el)
        index += 1
        new_el += 1
    return new_list
