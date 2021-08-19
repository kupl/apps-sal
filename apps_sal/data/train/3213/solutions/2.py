import re


def sum_of_a_beach(beach):
    return len(re.findall('sand|water|fish|sun', beach, flags=re.I))
