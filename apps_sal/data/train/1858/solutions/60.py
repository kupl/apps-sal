class FindElements:

    def __init__(self, root: TreeNode):
        self.all = []

        def helperIter(root):
            val = 0
            if not root:
                return
            stack = [(root, val)]
            while stack:
                (curr, val) = stack.pop()
                curr.val = val
                if curr.left:
                    self.all.append(2 * val + 1)
                    stack.append((curr.left, 2 * val + 1))
                if curr.right:
                    self.all.append(2 * val + 2)
                    stack.append((curr.right, 2 * val + 2))

        def helper(root, val):
            if not root:
                return
            if root:
                root.val = val
                self.all.append(val)
            if root.left:
                helper(root.left, 2 * val + 1)
            if root.right:
                helper(root.right, 2 * val + 2)
        helperIter(root)

    def find(self, target: int) -> bool:
        return target in self.all
