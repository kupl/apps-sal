class FindElements:

    def __init__(self, root: TreeNode):
        stack = [root]
        root.val = 0
        self.l = []
        while stack:
            r = stack.pop()
            self.l.append(r.val)
            if r.left:
                stack.append(r.left)
                r.left.val = 2 * r.val + 1
            if r.right:
                stack.append(r.right)
                r.right.val = 2 * r.val + 2

    def find(self, target: int) -> bool:
        return target in self.l
