def count_repeats(s): return sum(sum(1 for _ in n) - 1 for _, n in __import__("itertools").groupby(s))
