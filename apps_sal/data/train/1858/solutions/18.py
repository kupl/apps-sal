class FindElements:

    def __init__(self, root: TreeNode):
        self.root = root
        self.exists = set()

        def inner(node: TreeNode, my_val: int):
            if not node:
                return
            self.exists.add(my_val)
            inner(node.left, 2 * my_val + 1)
            inner(node.right, 2 * my_val + 2)
        inner(self.root, 0)

    def find(self, target: int) -> bool:
        return target in self.exists
