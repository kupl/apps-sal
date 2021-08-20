from re import findall


def sum_from_string(string):
    return sum((int(a) for a in findall('\\d+', string)))
