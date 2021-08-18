class FindElements:

    def __init__(self, root: TreeNode):

        root.val = 0
        self.vals = []

        def trav(node, prev, isLeft):
            if node.val != 0:
                if isLeft:
                    val = 2 * prev + 1
                    node.val = val
                    self.vals.append(val)
                else:
                    val = 2 * prev + 2
                    node.val = val
                    self.vals.append(val)
            if node.left:
                trav(node.left, node.val, True)
            if node.right:
                trav(node.right, node.val, False)

        trav(root, 0, None)
        self.root = root

    def find(self, target: int) -> bool:

        return target in self.vals
