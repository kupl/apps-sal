import re
pattern = re.compile('(Ha)+|(ha)+')


def kooka_counter(laughing):
    return len(pattern.findall(laughing))
