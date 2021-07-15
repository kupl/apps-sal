import re;body_count=lambda s:bool(re.search('([A-Z]\d){5}\.-[A-Z]%\d\.\d\d\.',s))
