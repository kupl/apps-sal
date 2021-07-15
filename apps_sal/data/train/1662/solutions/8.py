def tree_by_levels(node):
    levels = {}
    def sweep(subnode, level):
        if subnode != None:
            levels[level] = levels.get(level, []) + [subnode.value]
            sweep(subnode.left,  level + 1)
            sweep(subnode.right, level + 1)
    sweep(node, 0)
    return sum((levels[k] for k in sorted(levels)), [])

