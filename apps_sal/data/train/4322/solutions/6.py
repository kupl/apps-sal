body_count=lambda s:bool(__import__('re').search(r'(?:[A-Z]\d){5}\.-[A-Z]%\d\.\d\d\.',s))
