import re

def solve(a, b):
    return bool(re.match(f"^{a.replace('*', '.*')}$", b))


# without re
#
#def solve(a, b):
#    if "*" in a:
#        s, e = a.split("*")
#        return b.startswith(s) and b.replace(s, "").endswith(e)
#    else:
#        return a == b

