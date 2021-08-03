def build_trie(*words):
    root = {}
    for word in words:
        branch = root
        length = len(word)
        for i in range(1, length + 1):
            length -= 1
            key = word[:i]
            if key not in branch:
                branch[key] = None
            if length and not branch[key]:
                branch[key] = {}
            branch = branch[key]
    return root
