class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        check = 0  # left = 1, right = 2
        count = 0
        self.res = 0

        def dfs(node, count, check):
            if node:
                if check == 1:  # from left
                    dfs(node.left, 0, 1)
                    dfs(node.right, count + 1, 2)
                elif check == 2:  # from right
                    dfs(node.left, count + 1, 1)
                    dfs(node.right, 0, 2)
                elif check == 0:  # from root
                    dfs(node.left, count, 1)
                    dfs(node.right, count, 2)
            self.res = max(self.res, count)
        dfs(root, count, check)
        return self.res
