from itertools import groupby
def radix_tree(*d):
    if not {i for i in d if i} : return {} 
    store = {}
    for i, j in groupby(sorted(d), lambda x: x[0]):
        words = list(j)
        if len(words) == 1 : store[words[0]] = {}
        else:
            common = next((j for j, i in enumerate(zip(*words)) if len(set(i)) != 1), len(min(words, key=len)))
            store[words[0][:common]] = radix_tree(*[i[common:] for i in words if i[common:]])
    return store
