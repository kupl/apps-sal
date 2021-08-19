import re


def how_many_bees(hive):
    if hive is None:
        return 0
    s = ' '.join((''.join(line) for hiveArr in (hive, zip(*hive)) for line in hiveArr))
    return len(re.findall('b(?=ee)|ee(?=b)', s))
