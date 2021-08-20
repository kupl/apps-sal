class FindElements:

    def __init__(self, root: TreeNode):
        self.root = root
        res = {}

        def helper(node, parent=None, left=False, right=False):
            if node:
                if parent is None:
                    node.val = 0
                    res[node.val] = 1
                else:
                    if left:
                        node.val = parent.val * 2 + 1
                        res[node.val] = 1
                    if right:
                        node.val = parent.val * 2 + 2
                        res[node.val] = 1
                helper(node.left, node, True, False)
                helper(node.right, node, False, True)
        helper(root)
        self.res = res
        print(root)

    def find(self, target: int) -> bool:
        return target in self.res
