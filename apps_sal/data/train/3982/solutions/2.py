import numpy as np
import time


def stat(strg):
    """
    Each part of the string is of the form: h|m|s
    Input: 01|15|59, 1|47|6, 01|17|20, 1|32|34, 2|3|17
    Output: Range: 00|47|18 Average: 01|35|15 Median: 01|32|34
    """
    if strg == '':
        return ''
    racetimes = strg.split(',')
    secondtimes = []
    for t in racetimes:
        (h, m, s) = t.split('|')
        seconds = int(h) * 3600 + int(m) * 60 + int(s)
        secondtimes.append(seconds)
    avgs = np.mean(secondtimes)
    ranges = max(secondtimes) - min(secondtimes)
    medians = np.median(secondtimes)
    avg = time.strftime('%H|%M|%S', time.gmtime(avgs))
    ra = time.strftime('%H|%M|%S', time.gmtime(ranges))
    med = time.strftime('%H|%M|%S', time.gmtime(medians))
    return 'Range: {} Average: {} Median: {}'.format(ra, avg, med)
