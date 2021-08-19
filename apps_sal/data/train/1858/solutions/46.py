class FindElements:

    def __init__(self, root: TreeNode):
        self.values = []
        self.tree = root

        def preorder(node, value):
            self.values.append(value)
            node.val = value
            if node.left:
                preorder(node.left, value * 2 + 1)
            if node.right:
                preorder(node.right, value * 2 + 2)
        preorder(root, 0)

    def find(self, target: int) -> bool:
        return target in self.values
