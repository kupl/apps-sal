sum_from_string=lambda s:sum([int(k) for k in __import__('re').findall(r'\d+',s)])
