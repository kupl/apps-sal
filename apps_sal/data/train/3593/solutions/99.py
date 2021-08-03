def capitalize(s, ind):
    s_list = [ch for ch in s]
    for i in ind:
        try:
            s_list[i] = s_list[i].upper()
        except IndexError:
            pass
    return "".join(s_list)
