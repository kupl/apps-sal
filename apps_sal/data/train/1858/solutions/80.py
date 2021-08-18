class FindElements:

    def __init__(self, root: TreeNode):
        root.val = 0
        self.recList = []
        self.recover(root)

    def recover(self, root):
        if root != None:
            self.recList.append(root.val)
            if root.left != None:
                root.left.val = 2 * root.val + 1
                self.recover(root.left)
            if root.right != None:
                root.right.val = 2 * root.val + 2
                self.recover(root.right)

    def find(self, target: int) -> bool:
        if target in self.recList:
            return True
        else:
            return False
