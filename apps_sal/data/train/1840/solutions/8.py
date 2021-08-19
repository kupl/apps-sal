class Solution:

    def longestZigZag(self, root: TreeNode) -> int:
        self.res = 0
        if root.left:
            self.dfs(root.left, 1, True, False)
        if root.right:
            self.dfs(root.right, 1, False, True)
        return self.res

    def dfs(self, node, count, prevL, prevR):
        if not node:
            return
        self.res = max(self.res, count)
        if prevL:
            self.dfs(node.left, 1, True, False)
            self.dfs(node.right, count + 1, False, True)
        if prevR:
            self.dfs(node.left, count + 1, True, False)
            self.dfs(node.right, 1, False, True)
