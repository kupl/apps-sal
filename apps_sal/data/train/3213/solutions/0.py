import re


def sum_of_a_beach(beach):
    return len(re.findall('Sand|Water|Fish|Sun', beach, re.IGNORECASE))
