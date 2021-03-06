class FindElements:

    def __init__(self, root: TreeNode):
        if not root:
            return root
        self.root = root
        self.root.val = 0
        self.vals = []
        self.vals.append(self.root.val)
        self.construct(self.root)
        print(self.vals)

    def construct(self, root):
        if root.left:
            root.left.val = 2 * root.val + 1
            self.vals.append(root.left.val)
            self.construct(root.left)
        if root.right:
            root.right.val = 2 * root.val + 2
            self.vals.append(root.right.val)
            self.construct(root.right)
        return root

    def find(self, target: int) -> bool:
        if target in self.vals:
            return True
        return False
