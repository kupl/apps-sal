import re


def arbitrate(busAccess, n):
    return re.sub(r'(0*1)?(.*)', lambda m: (m.group(1) or '') + '0' * len(m.group(2)), busAccess)
