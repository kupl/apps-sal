def number(lines):
    cur_index = 0
    for l in lines:
        lines [cur_index] = "{}: {}".format (cur_index + 1, l)
        cur_index += 1
    return lines

        
        

