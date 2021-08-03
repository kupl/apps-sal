import re


def is_valid(idn):
    return re.match(r'^[a-zA-Z_$][\w_$]*$', idn) is not None
