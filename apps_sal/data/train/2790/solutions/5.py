import re

def dup(lst):
    return [re.sub(r"(.)\1+", r"\1", stg) for stg in lst]
