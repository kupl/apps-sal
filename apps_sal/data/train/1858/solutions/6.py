class FindElements:

    def __init__(self, root: TreeNode):
        self.root = root
        values = set()

        def recover(head, val):
            if head is None:
                return
            head.val = val
            values.add(val)
            recover(head.left, val * 2 + 1)
            recover(head.right, val * 2 + 2)
        recover(root, 0)
        self.values = values

    def find(self, target: int) -> bool:
        return target in self.values
