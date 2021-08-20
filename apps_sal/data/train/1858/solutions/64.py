class FindElements:

    def __init__(self, root: TreeNode):
        root.val = 0
        self.list1 = []
        self.helper(root)

    def helper(self, root):
        if not root:
            return
        self.list1.append(root.val)
        if root.left:
            root.left.val = 2 * root.val + 1
        if root.right:
            root.right.val = 2 * root.val + 2
        self.helper(root.left)
        self.helper(root.right)

    def find(self, target: int) -> bool:
        if target in self.list1:
            return True
        return False
