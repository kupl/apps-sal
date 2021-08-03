def comm_check(l, p_l, comm_started):
    if (l == '/' and p_l == '*' and comm_started == 2):
        return 0
    if (comm_started == 1 and l == '\n'):
        return 0
    if (l == '-' and p_l == '-'):
        return 1
    elif (l == '*' and p_l == '/'):
        return 2
    else:
        return comm_started


def get_textliterals(pv_code):
    indices = []
    open_i = -1
    comm_start = 0
    for i in range(0, len(pv_code)):
        comm_start = comm_check(pv_code[i], pv_code[i - 1], comm_start)
        if pv_code[i] == '\'' and comm_start == 0:
            if open_i == -1:
                open_i = i
            else:
                if (i + 1 < len(pv_code) and i - 1 >= 0):
                    if (pv_code[i + 1] == '\'' or pv_code[i - 1] == '\''):
                        continue
                indices.append((open_i, i + 1))
                open_i = -1
    if open_i != -1:
        indices.append((open_i, len(pv_code)))
    return indices
