slogan_maker=lambda a:list(map(' '.join,__import__('itertools').permutations(dict.fromkeys(a))))
