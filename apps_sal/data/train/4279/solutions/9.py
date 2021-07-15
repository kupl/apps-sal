from collections import defaultdict
def group_in_10s(*l):
    if not l : return []    
    d = defaultdict(list)
    for i in l:
        d[int(str(i//10))].append(i)
    return [None if d[i] == [] else sorted(d[i]) for i in range(1 + max(d.keys()))]
