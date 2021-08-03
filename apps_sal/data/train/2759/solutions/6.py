interleave = lambda *a: sum([list(i) for i in __import__('itertools').zip_longest(*a)], [])
