def time_correct(t):
    if not t:
        return t
    if len(t) != 8:
        return None
    for x in range(8):
        if (x + 1) % 3 == 0:
            if t[x] != ':':
                return None
        else:
            if not t[x].isnumeric():
                return None
    hrs, mins, secs = (int(x) for x in t.split(':'))
    mins = mins + secs // 60
    hrs = (hrs + mins // 60) % 24
    mins, secs = mins % 60, secs % 60
    return str(hrs).zfill(2) + ':' + str(mins).zfill(2) + ':' + str(secs).zfill(2)
