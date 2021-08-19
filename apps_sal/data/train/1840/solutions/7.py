class Solution:

    def longestZigZag(self, root: TreeNode) -> int:
        if not root:
            return 0
        max_zig_zag = 0

        def dfs(node):
            if not node:
                return (0, 0)
            left = dfs(node.left)
            right = dfs(node.right)
            nonlocal max_zig_zag
            max_zig_zag = max(1 + left[1], 1 + right[0], max_zig_zag)
            return (1 + left[1], 1 + right[0])
        dfs(root)
        return max_zig_zag - 1
