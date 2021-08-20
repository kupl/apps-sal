class FindElements:

    def __init__(self, root: TreeNode):
        self.elements = []

        def traverse(node, x):
            self.elements.append(x)
            if node.left != None:
                traverse(node.left, 2 * x + 1)
            if node.right != None:
                traverse(node.right, 2 * x + 2)
        traverse(root, 0)

    def find(self, target: int) -> bool:
        return target in self.elements
