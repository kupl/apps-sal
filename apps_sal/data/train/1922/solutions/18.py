class Solution:

    def minCameraCover(self, root: TreeNode) -> int:
        covered = {None}
        self.ans = 0

        def dfs(node, par):
            if node:
                dfs(node.left, node)
                dfs(node.right, node)
                if par is None and node not in covered or node.left not in covered or node.right not in covered:
                    covered.update({node, par, node.right, node.left})
                    self.ans += 1
        dfs(root, None)
        return self.ans
