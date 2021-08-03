import re

pattern = re.compile(r"(Ha)+|(ha)+")


def kooka_counter(laughing):
    return len(pattern.findall(laughing))
