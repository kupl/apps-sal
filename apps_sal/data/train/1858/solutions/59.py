class FindElements:

    def __init__(self, root: TreeNode):
        self.root = root

        def recover(head, val):
            if not head:
                return
            head.val = val
            recover(head.left, val * 2 + 1)
            recover(head.right, val * 2 + 2)
        recover(root, 0)

    def find(self, target: int) -> bool:
        steps = bin(target + 1)[3:]
        head = self.root
        for s in steps:
            if not head:
                return False
            if s == '0':
                head = head.left
            else:
                head = head.right
        return head and head.val == target
