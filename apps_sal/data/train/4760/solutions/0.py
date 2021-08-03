class T:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def is_bst(node):

    def extract(node):
        if node is not None:
            yield from extract(node.left)
            yield node.value
            yield from extract(node.right)

    gen = extract(node)
    try:
        u, v = next(gen), next(gen)
    except StopIteration:
        return True

    cmp = u < v
    for w in gen:
        if cmp != (v < w):
            return False
        v = w
    return True
