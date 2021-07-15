from string import digits
trans = str.maketrans("", "", digits)
def string_clean(s):
    return s.translate(trans)


from functools import partial
from re import compile
string_clean = partial(compile("\d+").sub, "")
