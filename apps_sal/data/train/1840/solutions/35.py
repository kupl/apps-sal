class Solution:

    def longestZigZag(self, root: TreeNode) -> int:
        self.max_zigzag = 0

        def dfs(node, is_left, streak):
            if not node:
                return
            self.max_zigzag = max(self.max_zigzag, streak)
            if is_left:
                dfs(node.right, not is_left, streak + 1)
                dfs(node.right, is_left, 0)
            else:
                dfs(node.left, not is_left, streak + 1)
                dfs(node.left, is_left, 0)
        dfs(root, True, 0)
        dfs(root, False, 0)
        return self.max_zigzag
