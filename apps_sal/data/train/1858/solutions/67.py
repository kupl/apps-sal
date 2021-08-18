class FindElements:

    def __init__(self, root: TreeNode):
        self.data = []

        def walk(node, v):
            if(not node):
                return

            self.data.append(v)
            walk(node.left, 2 * v + 1)
            walk(node.right, 2 * v + 2)

        walk(root, 0)

    def find(self, target: int) -> bool:
        return target in self.data
