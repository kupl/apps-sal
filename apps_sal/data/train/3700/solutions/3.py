import re


def kooka_counter(laughing):
    return len(re.findall('(Ha|ha)\\1*', laughing))
