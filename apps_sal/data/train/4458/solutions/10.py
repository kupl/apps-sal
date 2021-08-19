import re


def time_correct(t):
    if t == '':
        return ''
    if not t or not re.search('[0-9][0-9]:[0-9][0-9]:[0-9][0-9]', t):
        return None
    time = list(map(int, t.split(':')))
    for i in range(2, 0, -1):
        time[i - 1] += 1 * time[i] // 60
        time[i] = ('0' + str(time[i] % 60))[-2:]
    time[0] = ('0' + str(time[0] % 24))[-2:]
    return ':'.join(time)
