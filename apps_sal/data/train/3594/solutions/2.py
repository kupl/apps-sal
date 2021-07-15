is_isogram=lambda s:1==isinstance(s,str)==len(set(__import__('collections').Counter(filter(str.isalpha,s.lower())).values()))
