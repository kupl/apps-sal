def capitalize(s, ind):
    split_s = list(s)
    for i in ind:
        try:
            split_s[i] = split_s[i].upper()
        except IndexError:
            pass
    return ''.join(split_s)
