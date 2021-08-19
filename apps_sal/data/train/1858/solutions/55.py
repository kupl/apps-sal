class FindElements:
    rootNode = None
    elements = None

    def __init__(self, root: TreeNode):
        root.val = 0
        self.rootNode = root
        self.elements = []
        self.recover(self.rootNode)

    def recover(self, node):
        self.elements.append(node.val)
        if node.left != None:
            node.left.val = 2 * node.val + 1
            self.recover(node.left)
        if node.right != None:
            node.right.val = 2 * node.val + 2
            self.recover(node.right)

    def find(self, target: int) -> bool:
        return target in self.elements
