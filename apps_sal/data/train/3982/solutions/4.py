from statistics import mean, median


def sec2time(s):
    return '%02d|%02d|%02d' % (s // 3600 % 60, s // 60 % 60, s % 60)


def stat(strg):
    if not strg:
        return ''
    data = sorted([sum((int(val) * 60 ** (2 - i) for (i, val) in enumerate(t.split('|')))) for t in strg.split(', ')])
    return 'Range: %s Average: %s Median: %s' % (sec2time(data[-1] - data[0]), sec2time(int(mean(data))), sec2time(median(data)))
