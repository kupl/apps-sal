import re


def asterisc_it(s):
    if isinstance(s, int):
        s = str(s)
    elif isinstance(s, list):
        s = ''.join(map(str, s))
    return re.sub(r'(?<=[02468])(?=[02468])', '*', s)
