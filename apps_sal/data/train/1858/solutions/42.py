class FindElements:

    def __init__(self, root: TreeNode):
        self.root = root
        self.root.val = 0
        queue = []
        queue.append(root)
        self.values = []
        while(len(queue) > 0):
            current = queue.pop(0)
            leftval = 2 * current.val + 1
            rightval = 2 * current.val + 2

            if(current.left is not None):
                current.left.val = leftval
                queue.append(current.left)
                self.values.append(current.left.val)
            if(current.right is not None):
                current.right.val = rightval
                queue.append(current.right)
                self.values.append(current.right.val)

    def find(self, target: int) -> bool:
        if (target in self.values):
            return True
