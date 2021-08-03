def is_isogram(s): return 1 == isinstance(s, str) == len(set(__import__('collections').Counter(filter(str.isalpha, s.lower())).values()))
