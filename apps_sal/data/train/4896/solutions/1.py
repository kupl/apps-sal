def build_trie(*words):
    d = {}
    for word in words:
        dd = d
        w, l = "", len(word)
        for c in word:
            w += c
            l -= 1
            if w not in dd:
                dd[w] = None
            if l and dd[w] is None:
                dd[w] = {}
            dd = dd[w]
    return d
