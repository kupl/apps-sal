class Solution:

    def pruneTree(self, root: TreeNode) -> TreeNode:

        def dfs(node):
            if not node:
                return False
            a1 = dfs(node.left)
            a2 = dfs(node.right)
            if not a1:
                node.left = None
            if not a2:
                node.right = None
            return node.val == 1 or a1 or a2
        return root if dfs(root) else None
