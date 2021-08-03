def center_of(chars):
    if chars == '':
        return ''
    chars = chars * 10000

    def n_int(n):
        return n * (n + 1) // 2
    center = ''
    c = 0
    i = 0
    while n_int(i) <= len(chars):
        if i % 2 != 0:
            c += 1
            pos_center = (n_int(i) - c)
            center += chars[pos_center]
        i += 1
    for x in range(1, len(center)):
        subcenter = center[:x]
        if subcenter * (len(center) // len(subcenter)) + (subcenter[:len(center) % len(subcenter)]) == center:
            return(subcenter)
