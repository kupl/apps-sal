import re


def dad_filter(string):
    return re.sub('((?<=\\,)\\,+|[\\s,]+\\Z)', '', string)
