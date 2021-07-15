double_check = lambda s: bool(__import__('re').search(r'(?i)(.)\1',s))
