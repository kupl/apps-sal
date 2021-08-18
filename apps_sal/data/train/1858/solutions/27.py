class FindElements:

    def __init__(self, root: TreeNode):
        self.root = root
        res = []

        def helper(node, parentVal=None, left=False, right=False):
            if node:
                if parentVal is None:
                    val = 0
                    res.append(val)
                else:
                    if left:
                        val = parentVal * 2 + 1
                        res.append(val)
                    if right:
                        val = parentVal * 2 + 2
                        res.append(val)
                helper(node.left, val, True, False)
                helper(node.right, val, False, True)
        helper(root)
        self.res = set(res)
        print(root)

    def find(self, target: int) -> bool:
        return target in self.res
