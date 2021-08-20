import re
import statistics as st
P = re.compile('(\\d+)\\|(\\d+)\\|(\\d+)')


def s_to_h(time):
    (h, r) = divmod(time, 3600)
    (m, s) = divmod(r, 60)
    return f'{str(int(h)).zfill(2)}|{str(int(m)).zfill(2)}|{str(int(s)).zfill(2)}'


def stat(strg):
    t = P.findall(strg)
    if not strg:
        return ''
    s = [int(h) * 60 * 60 + int(m) * 60 + int(sec) for (h, m, sec) in t]
    (range, mean, median) = (max(s) - min(s), st.mean(s), st.median(s))
    return f'Range: {s_to_h(range)} Average: {s_to_h(mean)} Median: {s_to_h(median)}'
