class T:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def walk_tree(node):
    if node is None:
        return []

    return walk_tree(node.left) + [node.value] + walk_tree(node.right)


def is_bst(node):
    vals = walk_tree(node)
    ordered = vals[:]
    ordered.sort()
    return (ordered == vals) or (ordered == vals[::-1])
