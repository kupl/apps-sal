def tree_by_levels(node):
    return [v for (v, _, _) in sorted(extract_nodes(node), key=lambda x: (x[1], x[2]))]


def extract_nodes(node, lvl=0, directions=[]):
    if node:
        return [(node.value, lvl, directions)] + extract_nodes(node.left, lvl + 1, directions + [-1]) + extract_nodes(node.right, lvl + 1, directions + [1])
    return []
