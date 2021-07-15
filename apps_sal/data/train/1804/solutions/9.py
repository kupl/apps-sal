def recoverSecret(triplets):
    'triplets is a list of triplets from the secrent string. Return the string.'
    res = ""
    table = {}
    visited = set()
    for a,b,c in triplets:
        if not table.has_key(a):
            table[a] = set()
        if not table.has_key(b):
            table[b] = set()
        if not table.has_key(c):
            table[c] = set()
        table[a].add(b)
        table[a].add(c)
        table[b].add(c)

    count = len(table.keys())
    while len(visited) < count:
        Min = count
        c = ''
        for k,v in table.iteritems():
            l = len([elem for elem in v if elem not in visited])
            if l < Min and k not in visited:
                Min = l
                c = k
        visited.add(c)
        res += c
    return res[::-1]
