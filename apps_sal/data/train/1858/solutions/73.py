class FindElements:

    def __init__(self, root: TreeNode):
        self.root = root
        self.root.val = 0
        self.arr = []
        self.fix(self.root)

    def fix(self, currentNode):
        self.arr.append(currentNode.val)
        if currentNode.left:

            currentNode.left.val = 2 * currentNode.val + 1
            self.fix(currentNode.left)
        if currentNode.right:

            currentNode.right.val = 2 * currentNode.val + 2
            self.fix(currentNode.right)

    def find(self, target: int) -> bool:

        if target in self.arr:
            return True
        else:
            return False
