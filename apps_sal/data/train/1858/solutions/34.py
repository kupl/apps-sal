class FindElements:

    def __init__(self, root: TreeNode):
        root.val = 0
        nodes = [root]
        self.elements = [root.val]
        while nodes:
            node = nodes.pop(0)
            val = node.val
            if node.right is not None:
                self.elements.append(2 * val + 2)
                node.right.val = 2 * val + 2
                nodes.append(node.right)
            if node.left is not None:
                self.elements.append(2 * val + 1)
                node.left.val = 2 * val + 1
                nodes.append(node.left)

    def find(self, target: int) -> bool:
        try:
            value = self.elements.index(target)
            return True
        except ValueError:
            return False
