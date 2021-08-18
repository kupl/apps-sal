class FindElements:

    def __init__(self, root: TreeNode):

        self.ans = []

        def dfs(node, x):
            if not node:
                return

            node.val = x
            self.ans.append(x)
            dfs(node.left, 2 * x + 1)
            dfs(node.right, 2 * x + 2)

            return

        dfs(root, 0)

    def find(self, target: int) -> bool:
        return target in self.ans
