def find_longest(l):
    m, c = max(list(map(lambda x: len(str(x)), l))), 0
    for i in list(map(lambda x: len(str(x)), l)):
        if i == m:
            return l[c]
        c += 1
