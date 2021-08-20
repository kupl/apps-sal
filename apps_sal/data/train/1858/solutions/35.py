class FindElements:

    def __init__(self, root: TreeNode):
        self.result = []
        q = []
        if root is None:
            return False
        q.append((root, 0))
        self.result.append(0)
        while len(q) > 0:
            (node, value) = q.pop(0)
            if node.left is not None:
                temp = value * 2 + 1
                self.result.append(temp)
                q.append((node.left, temp))
            if node.right is not None:
                temp = value * 2 + 2
                self.result.append(temp)
                q.append((node.right, temp))
        print(self.result)

    def find(self, target: int) -> bool:
        return True if target in self.result else False
