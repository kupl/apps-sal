from collections import OrderedDict


def common_ground(s1, s2):
    return " ".join(filter(set(s1.split()).__contains__, OrderedDict.fromkeys(s2.split()))) or "death"
