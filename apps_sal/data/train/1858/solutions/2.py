class FindElements:

    def __init__(self, root: TreeNode):
        self.root = root
        self.values = set()

        def recover(head, val):
            if head is None:
                return
            head.val = val
            self.values.add(val)
            recover(head.left, val * 2 + 1)
            recover(head.right, val * 2 + 2)
        recover(root, 0)

    def find(self, target: int) -> bool:
        return target in self.values
