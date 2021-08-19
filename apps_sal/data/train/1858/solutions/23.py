def revalue(n, v):
    if n is None:
        return
    n.val = v
    revalue(n.left, 2 * v + 1)
    revalue(n.right, 2 * v + 2)


class FindElements:

    def __init__(self, root: TreeNode):
        self.root = root
        revalue(root, 0)

    def find(self, target: int) -> bool:
        if target == 0:
            return self.root is not None
        path = []
        otarget = target
        while target:
            branch = target % 2
            target //= 2
            if branch == 0:
                target -= 1
            path.append(branch)
        n = self.root
        while path:
            if path.pop():
                n = n.left
            else:
                n = n.right
            if n is None:
                return False
            if n.val == otarget:
                return True
        return False
