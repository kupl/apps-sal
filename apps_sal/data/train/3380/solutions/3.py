look_and_say_sequence = l = lambda s, n: n > 1 and l(''.join(str(len(list(g))) + k for k, g in __import__('itertools').groupby(s)), n - 1) or s
