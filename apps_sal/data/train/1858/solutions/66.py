class FindElements:

    def __init__(self, root: TreeNode):
        self.root = root
        self.vals = []
        self.createTree(root, 0)

    def createTree(self, root, val):
        root.val = val
        self.vals.append(val)
        if root.left is not None:
            self.createTree(root.left, 2 * root.val + 1)
        if root.right is not None:
            self.createTree(root.right, 2 * root.val + 2)

    def find(self, target: int) -> bool:
        return target in self.vals

    def findRec(self, target, root):
        if root.val == target:
            return True
        if root.left is not None:
            if self.findRec(target, root.left):
                return True
        if root.right is not None:
            if self.findRec(target, root.right):
                return True
        return False
