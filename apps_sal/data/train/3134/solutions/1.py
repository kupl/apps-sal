import re
def is_valid(id): return bool(re.match('^[a-z_$][\w$]*$', id, re.I))
