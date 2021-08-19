import re


def count_smileys(arr):
    return sum((1 for s in arr if re.match('\\A[:;][-~]?[)D]\\Z', s)))
