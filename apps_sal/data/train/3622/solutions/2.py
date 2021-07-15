import re
validate_usr = lambda str: bool(re.match('^[a-z\d_]{4,16}$', str))
