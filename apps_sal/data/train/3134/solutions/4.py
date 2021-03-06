import re


def is_valid(idn):
    return bool(re.match('[a-z_$][a-z0-9_$]*$', idn, flags=re.IGNORECASE))
