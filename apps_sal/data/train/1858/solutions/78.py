class FindElements:

    def __init__(self, root: TreeNode):
        root.val = 0
        stack = [root]
        self.values = []
        while stack:
            cur = stack.pop()
            if cur.right:
                cur.right.val = cur.val * 2 + 2
                self.values.append(cur.right.val)
                stack.append(cur.right)
            if cur.left:
                cur.left.val = cur.val * 2 + 1
                self.values.append(cur.left.val)
                stack.append(cur.left)

    def find(self, target: int) -> bool:
        if target in self.values:
            return True
        return False
