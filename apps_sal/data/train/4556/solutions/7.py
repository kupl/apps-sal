def count_me(s): return s.isdigit() and ''.join(str(len(list(g))) + k for k, g in __import__('itertools').groupby(s)) or ''
