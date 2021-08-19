import re


def find_nth_occurrence(substring, string, occurrence):
    try:
        return [s.start() for s in re.finditer('(?=' + substring + ')', string)][occurrence - 1]
    except:
        return -1
