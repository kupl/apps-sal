def is_valid_int(s):
    if len(s) != 2:
        return False

    try:
        int(s)
        return True
    except ValueError:
        return False


def time_correct(t):

    if t == None:
        return None
    elif t == "":
        return ""

    t_lst = t.split(':')

    if len(t_lst) != 3:
        return None

    if not is_valid_int(t_lst[0]) or not is_valid_int(t_lst[1]) or not is_valid_int(t_lst[2]):
        return None

    t_lst = [int(val) for val in t_lst]

    seconds = t_lst[2]
    minutes = t_lst[1]
    hours = t_lst[0]

    if seconds > 59:
        minutes += int(seconds / 60)
        seconds = seconds % 60

    if minutes > 59:
        hours += int(minutes / 60)
        minutes = minutes % 60

    if hours >= 24:
        hours = int(hours % 24)

    return '{:02d}:{:02d}:{:02d}'.format(hours, minutes, seconds)
