class T:

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def is_bst(node):

    def to_arr(t):
        return to_arr(t.left) + [t.value] + to_arr(t.right) if t else []
    arr = to_arr(node)
    s = sorted(arr)
    return s == arr or s == arr[::-1]
