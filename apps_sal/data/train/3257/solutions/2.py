def slogan_maker(a): return list(map(' '.join, __import__('itertools').permutations(dict.fromkeys(a))))
