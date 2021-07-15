import re
is_valid_HK_phone_number = lambda n:re.match('^\d{4} \d{4}$', n) is not None
has_valid_HK_phone_number = lambda n: re.match('.*\d{4} \d{4}.*', n) is not None

