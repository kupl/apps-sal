class FindElements:

    def __init__(self, root: TreeNode):
        self.values = []

        def evaluate(node, value):
            if not node:
                return
            node.val = value
            self.values.append(value)
            evaluate(node.left, value * 2 + 1)
            evaluate(node.right, value * 2 + 2)
        evaluate(root, 0)

    def find(self, target: int) -> bool:
        return target in self.values
