def what_is_the_time(time_in_mirror):
    (h, m) = map(int, time_in_mirror.split(':'))
    return '{:02}:{:02}'.format(-(h + (m != 0)) % 12 or 12, -m % 60)
