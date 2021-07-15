import re

def is_alt(s):
    return not re.search('[aeiou]{2}|[^aeiou]{2}',s)
