class FindElements:

    def __init__(self, root: TreeNode):
        self.val = []
        root.val = 0
        self.root = self.helper(root)

    def helper(self, root):
        if root:
            self.val.append(root.val)
            if root.left:
                root.left.val = 2 * root.val + 1
                l = self.helper(root.left)
            if root.right:
                root.right.val = 2 * root.val + 2
                r = self.helper(root.right)
            return root
        return

    def find(self, target: int) -> bool:
        return target in self.val
    'def helper2(self, root, target):\n        if root:\n            if root.val == target:\n                return True\n            if root.val \n            l = self.helper2(root.left, target)\n            r = self.helper2(root.right, target)\n            return l or r  \n        return False\n    '
