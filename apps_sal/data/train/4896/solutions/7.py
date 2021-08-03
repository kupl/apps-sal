def build_trie(*words):
    trie = {}
    for word in words:
        trie = insert(trie, build_branch(word) if word else {})
    return trie


def build_branch(word, i=0):
    if i < len(word):
        return {word[:i + 1]: build_branch(word, i + 1)}


def insert(trie, branch):
    if branch and trie:
        k, v = next(iter(list(branch.items())))
        if k in trie:
            trie[k] = insert(trie.get(k, {}), v)
        else:
            trie[k] = v
    return trie or branch
