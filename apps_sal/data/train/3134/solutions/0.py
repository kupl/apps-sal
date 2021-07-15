import re

def is_valid(idn):
    return re.compile('^[a-z_\$][a-z0-9_\$]*$', re.IGNORECASE).match(idn) != None
