import re

def get_age(s):
    return int(re.search(r"\d+", s).group(0))
