import re


def max_consec_zeros(n):
    return 'zero one two three four five six seven eight nine ten eleven twelve thirteen'.split()[max(map(len, re.findall('0+', format(int(n), 'b'))), default=0)].capitalize()
