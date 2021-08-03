import re


def get_age(age):
    an = re.sub(r'\D+', "", age)
    rean = int(an)
    return rean
