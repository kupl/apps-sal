def number(lines):
    x2 = 1
    new_list = []
    for x in lines:
        new_list.append(f"{str(x2)}: {x}")
        x2 += 1
    return new_list
