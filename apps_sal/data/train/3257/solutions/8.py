import itertools


def slogan_maker(tab):
    tab_set = set()
    unique = [x for x in tab if x not in tab_set and (tab_set.add(x) or True)]
    generator = [] * len(unique)
    x = list(itertools.permutations(unique))
    for i in x:
        generator.append(" ".join(i))
    return generator
