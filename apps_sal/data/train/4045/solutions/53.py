def number(lines):
    count = 0
    temp_list = []
    for i in lines:
        count += 1
        temp_list.append(str(count) + ': ' + i)
    return temp_list
