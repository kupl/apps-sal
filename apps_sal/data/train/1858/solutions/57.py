class FindElements:

    def __init__(self, root: TreeNode):
        self.root = root
        self.values = list()
        self.regen(root, 0)

    def find(self, target: int) -> bool:
        return target in self.values

    def regen(self, root, v):
        if root == None:
            return
        root.val = v
        self.values.append(v)
        self.regen(root.left, 2 * v + 1)
        self.regen(root.right, 2 * v + 2)
