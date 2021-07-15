remove=lambda s:' '.join(r for r,_ in __import__('re').findall(r'((!*)\w+\2)',s))
