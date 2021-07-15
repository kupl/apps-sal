def seven_ate9(str_in):
    if len(str_in) < 3:
        return str_in
    str_out = str_in[0]
    for i, c in enumerate(str_in[1:-1], 1):
        if c == '9':
            if str_in[i - 1] == '7' and str_in[i + 1] == '7':
                continue
        str_out += c
    return str_out + str_in[-1]
