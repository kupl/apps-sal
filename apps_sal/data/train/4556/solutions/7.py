count_me=lambda s:s.isdigit()and''.join(str(len(list(g)))+k for k,g in __import__('itertools').groupby(s))or''
