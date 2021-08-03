def validPhoneNumber(x): return bool(__import__('re').match('\(\d{3}\) \d{3}-\d{4}$', x))
