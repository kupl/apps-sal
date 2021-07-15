class FindElements:

    def __init__(self, root: TreeNode):
        self.value_set = set()
        root.val = 0
        self.recover_tree(root)

    def recover_tree(self, root):
        if root:
            self.value_set.add(root.val)
            if root.left:
                root.left.val = 2 * root.val + 1
                self.recover_tree(root.left)
            if root.right:
                root.right.val = 2 * root.val + 2
                self.recover_tree(root.right)
        return root

    def find(self, target: int) -> bool:
        return target in self.value_set
