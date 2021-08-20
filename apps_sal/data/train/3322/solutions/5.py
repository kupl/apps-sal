def cypher(s):
    doc = [['', 'I', 'R', 'E', 'A', 'S', 'G', 'T', 'B', ' ', 'O'], ['', 'l', 'z', 'e', 'a', 's', 'b', 't', ' ', 'g', 'o']]
    return ' '.join((''.join((e if e not in doc[e.islower()] else str(doc[e.islower()].index(e))[-1] for e in x)) for x in s.split(' ')))
