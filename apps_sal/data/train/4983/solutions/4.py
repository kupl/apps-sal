from collections import defaultdict

def merge(*dicts):
    d = defaultdict(list)
    [d[key].append(value) for dictionary in dicts for key, value in list(dictionary.items()) ]
    return d
    

