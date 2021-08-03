def build_trie(*Q):
    R = {'': {}}
    for V in Q:
        for B in range(len(V)):
            B = V[:1 + B]
            if not B in R:
                if not R[B[:-1]]:
                    R[B[:-2]][B[:-1]] = R[B[:-1]] = {}
                R[B[:-1]][B] = R[B] = None
    return R['']
