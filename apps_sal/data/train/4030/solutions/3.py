from os.path import commonprefix

def radix_tree(*words):
    groups = {}
    for word in words:
        if word:
            groups[word[0]] = groups.get(word[0], []) + [word]
    root = {}
    for group in groups.values():
        prefix = commonprefix(group)
        root[prefix] = radix_tree(*(w[len(prefix):] for w in group))
    return root
