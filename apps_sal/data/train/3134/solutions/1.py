import re
is_valid = lambda id: bool(re.match('^[a-z_$][\w$]*$', id, re.I))
