class T:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def is_bst(node):
    def traverse(n):
        return [] if not n else traverse(n.left) + [n.value] + traverse(n.right)
    vals = traverse(node)
    zipped = list(zip(vals, vals[1:]))
    return all(a < b for a, b in zipped) or all(a > b for a, b in zipped)
