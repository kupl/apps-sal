class Solution:

    def goodNodes(self, root: TreeNode) -> int:
        res = [0]

        def dfs(node, m):
            if not node:
                return
            if node.val >= m:
                res[0] += 1
            dfs(node.left, max(node.val, m))
            dfs(node.right, max(node.val, m))
        dfs(root, root.val)
        return res[0]
