class T:
    def __init__(self, value, left=None, right=None):
        self.value, self.left, self.right = value, left, right


def is_bst(node):
    def walk(node, from_, to_, min_=float('-inf'), max_=float('inf')):
        return node is None or min_ <= node.value <= max_ \
            and walk(getattr(node, from_), from_, to_, min_, node.value) \
            and walk(getattr(node, to_), from_, to_, node.value, max_)
    return walk(node, 'left', 'right') or walk(node, 'right', 'left')
