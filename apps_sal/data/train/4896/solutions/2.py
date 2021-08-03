def build_trie(*words):
    trie = {}
    for word in words:
        node = trie
        l = len(word)
        for i in range(1, l + 1):
            w = word[:i]
            node[w] = node = {} if l - i and node.get(w) is None else node.get(w)
    return trie
