def what_is_the_time(time_in_mirror):
    if not time_in_mirror:
        return
    x, y = map(int, time_in_mirror.split(':'))
    q, r = divmod(720 - 60 * x - y, 60)
    return "{:02d}:{:02d}".format(q % 12 or 12, r)
