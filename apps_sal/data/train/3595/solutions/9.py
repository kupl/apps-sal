from collections import Counter


def swap(s1, s2):
    temp = [("", "")] + [(f"{k}{k.upper()}", f"{k.upper()}{k}") for k, v in Counter(s1.lower()).items() if v & 1]
    return s2.translate(str.maketrans(*map(''.join, zip(*temp))))


def work_on_strings(a, b):
    return swap(b, a) + swap(a, b)
