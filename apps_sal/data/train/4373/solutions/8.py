import re


def count_smileys(arr):
    count = 0
    for i in arr:
        p = re.compile("^[:;][-~]*[)D]")
        if p.match(i):
            count += 1
    return count
