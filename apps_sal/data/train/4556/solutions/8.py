from itertools import groupby
import re

def count_me(data):
    s = ''.join(str(len(list(g)))+k for k,g in groupby(data))
    return s if re.search(r'[a-zA-Z]', s) is None else ''
