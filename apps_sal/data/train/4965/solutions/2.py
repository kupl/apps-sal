import re


def sum_of_integers_in_string(s):
    return sum(int(i) for i in re.findall('\d+', s))
