def get_military_time(s):
    delta = 12 * s.endswith('PM')
    h, m, s = s[:-2].split(':')
    hour = int(h) + delta
    return '{:02}:{}:{}'.format(12 if hour == 24 else 0 if hour == 12 else hour, m, s)
