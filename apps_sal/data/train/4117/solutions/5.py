def sum_from_string(s): return sum([int(k) for k in __import__('re').findall(r'\d+', s)])
