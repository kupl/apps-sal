import re


def get_age(age):
    an = re.sub('\\D+', '', age)
    rean = int(an)
    return rean
