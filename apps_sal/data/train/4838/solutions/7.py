import re


def find_nth_occurrence(substring, string, occurrence=1):
    try:
        return [m.start() for m in re.finditer(f'(?={substring})', string)][occurrence - 1]
    except:
        return -1
