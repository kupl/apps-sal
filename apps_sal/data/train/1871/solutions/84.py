class Solution:

    def dfs(self, root, ancestors):
        if ancestors:
            for anc in ancestors:
                potential = abs(root.val - anc)
                if potential > self.ans:
                    self.ans = potential
        if root.left:
            self.dfs(root.left, ancestors + [root.val])
        if root.right:
            self.dfs(root.right, ancestors + [root.val])

    def maxAncestorDiff(self, root: TreeNode) -> int:
        self.ans = 0
        self.dfs(root, [])
        return self.ans
