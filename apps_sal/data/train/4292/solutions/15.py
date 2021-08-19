import re


def string_clean(s):
    """
    Function will return the cleaned string
    """
    return re.sub('[\\d+]', '', s)
