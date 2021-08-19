def super_pad(string, width, fill=' '):
    str_len = len(string)
    if fill.find('>') + 1:
        fill = fill[1:]
        fill_len = len(fill)
        to_fill_len = width - str_len
        if width < str_len:
            retval = string[0:width]
        elif fill_len == 0:
            retval = string
        elif fill_len == 1:
            RHS_to_fill = width - str_len
            retval = string + fill * RHS_to_fill
        elif fill_len > 1:
            chunks = int(to_fill_len / fill_len)
            parts = to_fill_len % fill_len
            total_len = chunks * fill_len + parts
            retvalb = string + (fill * (chunks + 1))[0:total_len]
            retval = retvalb
        else:
            retval = 'RIGHT: Oops'
    elif fill.find('^') + 1:
        fill = fill[1:]
        fill_len = len(fill)
        to_fill_len = int((width - str_len) / 2)
        LHS_to_fill_len = to_fill_len + (width - str_len) % 2
        RHS_to_fill_len = to_fill_len
        if width < str_len:
            retval = string[0:width]
        elif fill_len == 0:
            retval = string
        else:
            LHS_chunks = int(LHS_to_fill_len / fill_len)
            LHS_parts = LHS_to_fill_len % fill_len
            LHS_total_len = LHS_chunks * fill_len + LHS_parts
            RHS_chunks = int(RHS_to_fill_len / fill_len)
            RHS_parts = RHS_to_fill_len % fill_len
            RHS_total_len = RHS_chunks * fill_len + RHS_parts
            retval = (fill * (LHS_chunks + 1))[0:LHS_total_len] + string + (fill * (RHS_chunks + 1))[0:RHS_total_len]
    else:
        if fill.find('<') + 1:
            fill = fill[1:]
        fill_len = len(fill)
        if width < str_len:
            retval = string[str_len - width:]
        elif fill_len == 0:
            retval = string
        elif fill_len == 1:
            LHS_to_fill = width - str_len
            retval = fill * LHS_to_fill + string
        elif fill_len > 1:
            LHS_to_fill = width - str_len
            fill_count = int(LHS_to_fill / fill_len)
            fill_count_rem = LHS_to_fill % fill_len
            retval = fill * fill_count + fill[0:fill_count_rem] + string
        else:
            retval = 'Left_TEST_Left'
    return retval
