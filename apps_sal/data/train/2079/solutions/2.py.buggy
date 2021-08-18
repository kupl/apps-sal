
def add_edges(s1, s2, w):
    nonlocal edges
    i = 0
    while i < len(s1) and i < len(s2) and s1[i] == s2[i]:
        i += 1
    j = len(s1)
    while j > i:
        if s1[:j] in edges:
            edges[s1[:j]] += w
        else:
            edges[s1[:j]] = w
        j -= 1
    j = len(s2)
    while j > i:
        if s2[:j] in edges:
            edges[s2[:j]] += w
        else:
            edges[s2[:j]] = w
        j -= 1


def way(s1, s2):
    nonlocal edges
    i = 0
    while i < len(s1) and i < len(s2) and s1[i] == s2[i]:
        i += 1
    w = 0
    j = len(s1)
    while j > i:
        if s1[:j] in edges:
            w += edges[s1[:j]]
        j -= 1
    j = len(s2)
    while j > i:
        if s2[:j] in edges:
            w += edges[s2[:j]]
        j -= 1
    return w


q = int(input())
edges = dict()
for i in range(q):
    l = list(map(int, input().split()))
    if l[0] == 1:
        l[1] = bin(l[1])
        l[1] = l[1][2:]
        l[2] = bin(l[2])
        l[2] = l[2][2:]
        add_edges(l[1], l[2], l[3])
    if l[0] == 2:
        l[1] = bin(l[1])
        l[1] = l[1][2:]
        l[2] = bin(l[2])
        l[2] = l[2][2:]
        print(way(l[1], l[2]))
