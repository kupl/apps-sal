from re import match, search

is_valid_HK_phone_number = lambda n: match('^\d{4} \d{4}$', n) is not None
has_valid_HK_phone_number = lambda n: search('\d{4} \d{4}', n) is not None
