def time_correct(t):
    if t == "":
        return ""
    elif t == None:
        return None
    elif len(t) != 8 or len(t.split(':')) != 3 or not all(x.isdigit() for x in t.split(':')):
        return None

    t_list = [int(x) for x in t.split(':')]
    if t_list[2] > 59:
        t_list[1] += 1
        t_list[2] -= 60
    if t_list[1] > 59:
        t_list[0] += 1
        t_list[1] -= 60
    while t_list[0] >= 24:
        t_list[0] -= 24
    return '{:02d}:{:02d}:{:02d}'.format(t_list[0], t_list[1], t_list[2])
