class FindElements:
    treeroot = TreeNode()
    l = []

    def __init__(self, root: TreeNode):

        def correct(root):
            if root:
                if root.right:
                    root.right.val = 2 * root.val + 2
                    correct(root.right)
                if root.left:
                    root.left.val = 2 * root.val + 1
                    correct(root.left)
            return
        root.val = 0
        correct(root)
        self.treeroot = root
        self.l = self.inorder(self.treeroot)

    def inorder(self, root):
        if root:
            return self.inorder(root.left) + [root.val] + self.inorder(root.right)
        return []

    def find(self, target: int) -> bool:
        return target in self.l
