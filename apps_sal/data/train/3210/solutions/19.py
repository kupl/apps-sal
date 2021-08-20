from collections import Counter


def get_strings(city):
    return ','.join([k.lower() + ':' + '*' * v for (k, v) in Counter(city.lower()).items() if k.isalpha()])
