def double_check(s): return bool(__import__('re').search(r'(?i)(.)\1', s))
