def xMasTree(n):
    hashtags = '#' * (n - 1)
    spaces = '_' * (n - 1)
    tree = []
    for i in range(n):
        left = spaces[i:] + hashtags[:i]
        tree.append(left + '#' + left[::-1])
    for i in range(2):
        tree.append(spaces + '#' + spaces)
    return tree
