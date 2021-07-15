def number(lines):
    out_lst = []
    line_num = 1
    for item in lines:
        out_lst.append(f'{line_num}: {item}')
        line_num += 1
    return out_lst
