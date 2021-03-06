class FindElements:

    def __init__(self, root: TreeNode):
        self.tree = root
        self.values = []
        from collections import deque
        stack = deque()
        stack.append(root)
        root.val = 0
        curr = root
        while stack:
            if curr:
                self.values.append(curr.val)
                if curr.left:
                    curr.left.val = 2 * curr.val + 1
                if curr.right:
                    curr.right.val = 2 * curr.val + 2
                    stack.append(curr.right)
                curr = curr.left
            else:
                curr = stack.pop()

    def find(self, target: int) -> bool:
        if target in self.values:
            return True
        else:
            return False
