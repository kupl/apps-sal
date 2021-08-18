def xMasTree(n):
    hashtags = '
    spaces = '_' * (n - 1)
    tree = []
    for i in range(n):
        left = spaces[i:] + hashtags[:i]
        tree.append(left + '
    for i in range(2):
        tree.append(spaces + '
    return tree
