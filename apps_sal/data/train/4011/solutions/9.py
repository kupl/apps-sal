import re


def get_free_urinals(u):
    return -1 if '11' in u else len(re.findall('(?<!1)0[0$]?(?!1)', u))
