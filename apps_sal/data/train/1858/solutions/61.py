class FindElements:

    def __init__(self, root: TreeNode):
        self.q = []

        def search(node, value):
            if node:
                self.q.append(value)
                search(node.left, value * 2 + 1)
                search(node.right, value * 2 + 2)
        search(root, 0)

    def find(self, target: int) -> bool:
        return target in self.q
