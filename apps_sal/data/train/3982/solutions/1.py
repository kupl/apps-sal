from statistics import median, mean


def stat(s):
    if not s:
        return ''
    t = [itime(w) for w in s.split(',')]
    return 'Range: {} Average: {} Median: {}'.format(stime(max(t) - min(t)), stime(int(mean(t))), stime(int(median(t))))


def itime(w):
    return sum([int(c) * 60 ** i for (i, c) in enumerate(w.split('|')[::-1])])


def stime(n):
    return '{:02d}|{:02d}|{:02d}'.format(n // 3600, n % 3600 // 60, n % 60)
