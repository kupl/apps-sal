def find_word(board, word):
    P = {(i, j): e for (j, r) in enumerate(board) for (i, e) in enumerate(r)}
    (chains, word) = ([[p] for p in P if P[p] == word[0]], word[1:])
    while word and chains:
        (c, word, newchains) = (word[0], word[1:], [])
        for chain in chains:
            (i, j) = chain[-1]
            neighbours = [(i + a, j + b) for a in range(-1, 2) for b in range(-1, 2)]
            newchains += [chain + [p] for p in neighbours if c == P.get(p, None) and p not in chain]
        chains = newchains
    return len(chains) > 0
