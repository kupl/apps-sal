import re


def get_free_urinals(urinals):
    return -1 if "11" in urinals else sum((1 + len(sub)) // 2 for sub in re.split(r"0?10?", urinals))
