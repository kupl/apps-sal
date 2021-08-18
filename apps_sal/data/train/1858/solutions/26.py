class FindElements:

    def __init__(self, root: TreeNode):
        self.root = root
        res = []

        def helper(node, parent=None, left=False, right=False):
            if node:
                if parent is None:
                    node.val = 0
                    res.append(node.val)
                else:
                    if left:
                        node.val = parent.val * 2 + 1
                        res.append(node.val)
                    if right:
                        node.val = parent.val * 2 + 2
                        res.append(node.val)
                helper(node.left, node, True, False)
                helper(node.right, node, False, True)
        helper(root)
        self.res = set(res)
        print(root)

    def find(self, target: int) -> bool:
        return target in self.res
