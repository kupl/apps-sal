class FindElements:

    def __init__(self, root: TreeNode):
        self.array = {}
        self.populate_array(root, 0)

    def populate_array(self, node, count):
        if not node:
            return
        self.array[count] = True
        self.populate_array(node.left, count * 2 + 1)
        self.populate_array(node.right, count * 2 + 2)

    def find(self, target: int) -> bool:
        return target in self.array
