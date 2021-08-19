from collections import Counter


def get_strings(city):
    d = dict(Counter(city.lower()))
    ret = [f"{k}:{v * '*'}" for (k, v) in d.items() if k.isalpha()]
    return ','.join(ret)
