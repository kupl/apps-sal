class Solution:
    def __init__(self):
        self.max_length = float('-inf')

    def longestZigZag(self, root):
        return self.dfs(root)[2] - 1

    def dfs(self, root):
        if root is None:
            return [0, 0, 0]

        left_res = self.dfs(root.left)
        right_res = self.dfs(root.right)

        maxForSubtree = max(left_res[1], right_res[0]) + 1
        return [left_res[1] + 1, right_res[0] + 1, max(maxForSubtree, left_res[2], right_res[2])]
