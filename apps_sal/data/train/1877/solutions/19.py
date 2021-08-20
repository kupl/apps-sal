class Solution:

    def sufficientSubset(self, root: TreeNode, limit: int) -> TreeNode:

        def dfs(node, path_sum):
            if not node:
                return False
            path_sum += node.val
            if not node.left and (not node.right):
                return path_sum >= limit
            left = dfs(node.left, path_sum)
            right = dfs(node.right, path_sum)
            if not left:
                node.left = None
            if not right:
                node.right = None
            return left or right
        result = dfs(root, 0)
        return root if result else None
