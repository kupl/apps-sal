def build_trie(*words):
    trie = {}
    for word in words:
        node = trie
        for i in range(1, len(word)+1):
            prefix = word[:i]
            if prefix not in node:
                node[prefix] = None
            if i < len(word) and node[prefix] is None:
                node[prefix] = {}
            node = node[prefix]
    return trie
