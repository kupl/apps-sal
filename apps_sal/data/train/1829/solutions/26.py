class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(node, m):
            if node == None:
                return 0
            value = 1 if node.val >= m else 0
            m = max(m, node.val)
            return dfs(node.right, m) + dfs(node.left, m) + value
        return dfs(root, -float(inf))
