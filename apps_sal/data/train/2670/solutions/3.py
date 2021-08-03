look_and_say_and_sum = l = lambda n, s='1': n < 2 and sum(map(int, s)) or l(n - 1, ''.join(str(len(list(g))) + k for k, g in __import__('itertools').groupby(s)))
