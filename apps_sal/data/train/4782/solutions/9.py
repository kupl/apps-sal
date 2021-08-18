import operator


def calc(tree, args):
    if tree.left is None:
        tree.left = args.pop(0)
    if isinstance(tree.left, Tree):
        tree.left = calc(tree.left, args)
    if tree.right is None:
        tree.right = args.pop(0)
    if isinstance(tree.right, Tree):
        tree.right = calc(tree.right, args)
    return tree.op(tree.left, tree.right)


class Tree:
    def __init__(self, left=None, op=None, right=None):
        self.left = left
        self.right = right
        self.op = op

    def __call__(self, *args):
        args = list(args)
        result = calc(self, args)
        self.__init__()
        return result

    def __add__(self, other):
        return self._left_op(other, operator.add)

    def __sub__(self, other):
        return self._left_op(other, operator.sub)

    def __mul__(self, other):
        return self._left_op(other, operator.mul)

    def __floordiv__(self, other):
        return self._left_op(other, operator.floordiv)

    def __radd__(self, other):
        return self._right_op(other, operator.add)

    def __rsub__(self, other):
        return self._right_op(other, operator.sub)

    def __rmul__(self, other):
        return self._right_op(other, operator.mul)

    def __rfloordiv__(self, other):
        return self._right_op(other, operator.floordiv)

    def _left_op(self, right, op):
        left = None
        if self.op:
            left = self
        current = Tree(left, op, right)
        if isinstance(right, Tree):
            if self is right:
                current.right = None
            elif right.op:
                current.right = Tree(right.left, right.op, right.right)
            else:
                current.right = None
        return current

    def _right_op(self, left, op):
        right = None
        if self.op:
            right = self
        current = Tree(left, op, right)
        if isinstance(left, Tree):
            if self is left:
                current.left = None
            elif left.op:
                current.left = Tree(left.left, left.op, left.right)
            else:
                current.left = None
        return current


x = Tree()
