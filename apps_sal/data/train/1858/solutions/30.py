class FindElements:

    def recoverTree(self, node: TreeNode, val: int) -> None:
        if node:
            node.val = val
            self.num_set.add(val)
            self.recoverTree(node.left, 2 * val + 1)
            self.recoverTree(node.right, 2 * val + 2)
        '\n        if not node.left and not node.right:\n            return None\n        if node.left:\n            node.left.val = 2 * node.val + 1\n            self.num_set.add(node.left.val)\n            self.recoverTree(node.left)\n        if node.right:\n            node.right.val = 2 * node.val + 2\n            self.num_set.add(node.right.val)\n            self.recoverTree(node.right)\n        '

    def __init__(self, root: TreeNode):
        self.num_set = set()
        self.num_set.add(0)
        self.recoverTree(root, 0)
        self.root = root

    def find(self, target: int) -> bool:
        if target < self.root.val:
            return False
        return target in self.num_set
