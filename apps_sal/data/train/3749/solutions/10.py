def expanded_form(num):
    (str_num, str_list, index_track) = (str(num), [], 0)
    for digit in str_num:
        if digit != str(0):
            val = int(digit) * 10 ** (len(str_num) - (index_track + 1))
            str_list.append(str(val))
        index_track += 1
    return ' + '.join(str_list)
