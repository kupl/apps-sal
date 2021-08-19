class Solution:

    def longestZigZag(self, root: TreeNode) -> int:
        self.res = 0
        self.helper(root, True)
        self.helper(root, False)
        return self.res - 1

    def helper(self, root, isLeft):
        if not root:
            return 0
        left = self.helper(root.left, True)
        right = self.helper(root.right, False)
        self.res = max(self.res, left + 1, right + 1)
        return right + 1 if isLeft else left + 1
