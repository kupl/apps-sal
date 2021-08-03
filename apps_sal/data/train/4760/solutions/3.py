class T:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def preorder(self):
    if not self:
        return []
    return [self.value] + preorder(self.left) + preorder(self.right)


def is_bst(T):
    if not (T and (T.left or T.right)):
        return True
    v, l, r, R1, R2 = T.value, T.left, T.right, True, True
    if l and max(preorder(l)) > v or r and min(preorder(r)) < v:
        R1 = False
    if l and min(preorder(l)) < v or r and max(preorder(r)) > v:
        R2 = False
    return is_bst(l) and is_bst(r) and (R1 or R2)
