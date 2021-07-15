from collections import defaultdict, deque

def processes(start, end, processes):
    D, L, S = defaultdict(dict), deque([(start, [])]), set()
    for a, b, c in processes: D[b][a] = c
    while L:
        current, path = L.pop()
        if current == end: return path
        if current not in S:
            S.add(current)
            for k,v in D[current].items():
                L.appendleft((v, path+[k]))
    return []
