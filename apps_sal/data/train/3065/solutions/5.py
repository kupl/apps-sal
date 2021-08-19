def get_textliterals(pv_code):
    l_list = []
    l_switch = 'empty'
    for i in range(len(pv_code)):
        if pv_code[i] == "'" and pv_code[i:i + 2] != "''" and (pv_code[i - 1:i + 1] != "''"):
            if l_switch == 'empty':
                l_begin = i
                l_switch = 'begin'
            elif l_switch == 'begin':
                l_list.append((l_begin, i + 1))
                l_switch = 'empty'
        elif pv_code[i:i + 2] == '--':
            if l_switch != 'begin' and l_switch != 'rem2':
                l_switch = 'rem1'
        elif pv_code[i:i + 2] == '/*':
            if l_switch != 'begin' and l_switch != 'rem1':
                l_switch = 'rem2'
        elif pv_code[i:i + 2] == '*/':
            if l_switch == 'rem2':
                l_switch = 'empty'
        elif pv_code[i] == '\n':
            if l_switch == 'rem1':
                l_switch = 'empty'
    if l_switch == 'begin':
        l_list.append((l_begin, i + 1))
    return l_list
