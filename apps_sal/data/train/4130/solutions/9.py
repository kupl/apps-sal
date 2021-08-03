import re
def is_valid_HK_phone_number(n): return re.match('^\d{4} \d{4}$', n) is not None
def has_valid_HK_phone_number(n): return re.match('.*\d{4} \d{4}.*', n) is not None
