class Solution:

    def longestZigZag(self, root: TreeNode) -> int:
        self.longest = 0
        self.dfs(root, 0, 0)
        return self.longest

    def dfs(self, node, longest_left, longest_right):
        self.longest = max(self.longest, longest_left, longest_right)
        if node.left:
            self.dfs(node.left, longest_right + 1, 0)
        if node.right:
            self.dfs(node.right, 0, longest_left + 1)
