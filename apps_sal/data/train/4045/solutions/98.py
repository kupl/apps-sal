def number(lines):
    numbered_lst = []
    line_num = 1
    for line in lines:
        numbered_lst.append(str(line_num)+": "+line)
        line_num += 1
    return numbered_lst
    

