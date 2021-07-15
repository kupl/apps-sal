def tree_by_levels(node):
    r = []
    nodes = [node]
    while nodes:
        r += [n.value for n in nodes if n]
        nodes = [e for n in [(n.left, n.right) for n in nodes if n] for e in n if e]
        
    return r
