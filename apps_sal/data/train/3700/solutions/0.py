import re


def kooka_counter(laughing):
    return len(re.findall('(ha)+|(Ha)+', laughing))
