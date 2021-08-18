class FindElements:
    def recoverTree(self, node: TreeNode, val: int) -> None:
        if node:
            node.val = val
            self.num_set.add(val)
            self.recoverTree(node.left, 2 * val + 1)
            self.recoverTree(node.right, 2 * val + 2)

        '''
        if not node.left and not node.right:
            return None
        if node.left:
            node.left.val = 2 * node.val + 1
            self.num_set.add(node.left.val)
            self.recoverTree(node.left)
        if node.right:
            node.right.val = 2 * node.val + 2
            self.num_set.add(node.right.val)
            self.recoverTree(node.right)
        '''

    def __init__(self, root: TreeNode):
        self.num_set = set()
        self.num_set.add(0)

        self.recoverTree(root, 0)
        self.root = root

    def find(self, target: int) -> bool:
        if target < self.root.val:
            return False
        return target in self.num_set
