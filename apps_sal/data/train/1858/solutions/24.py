class FindElements:

    def recover(self, node):
        if not node:
            return
        self.memo |= 1 << node.val
        if node.left:
            node.left.val = 2 * node.val + 1
            self.recover(node.left)
        if node.right:
            node.right.val = 2 * node.val + 2
            self.recover(node.right)

    def __init__(self, root: TreeNode):
        self.root = root
        self.root.val = 0
        self.memo = 0
        self.recover(self.root)

    def find(self, target: int) -> bool:
        return self.memo & (1 << target) != 0
