import re
validate_code = lambda c: bool(re.search("^[1-3]", str(c)))
