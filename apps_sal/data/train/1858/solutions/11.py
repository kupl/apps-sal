class FindElements:
    def recover(self, node, x):
        if node is None:
            return
        node.val = x
        self.vals.add(node.val)
        self.recover(node.left, (2 * node.val) + 1)
        self.recover(node.right, (2 * node.val) + 2)

    def __init__(self, root: TreeNode):
        root.val = 0
        self.vals = set()
        self._root = root
        self.recover(root, 0)

    def find(self, target: int) -> bool:
        return target in self.vals
