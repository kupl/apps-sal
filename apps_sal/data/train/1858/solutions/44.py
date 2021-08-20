class FindElements:

    def dfs(self, root, x, Node_vals):
        if not root:
            return
        root.val = x
        Node_vals.append(x)
        self.dfs(root.left, 2 * x + 1, Node_vals)
        self.dfs(root.right, 2 * x + 2, Node_vals)
        return Node_vals

    def __init__(self, root: TreeNode):
        self.N_V = self.dfs(root, 0, [])

    def find(self, target: int) -> bool:
        return target in self.N_V
