class FindElements:

    def __init__(self, root: TreeNode):
        self.data = set()

        def walk(node, v):
            if(not node):
                return

            self.data.add(v)
            walk(node.left, 2 * v + 1)
            walk(node.right, 2 * v + 2)

        walk(root, 0)

    def find(self, target: int) -> bool:
        return target in self.data
