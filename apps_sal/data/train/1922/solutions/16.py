class Solution:

    def helper(self, root):
        if not root:
            return 2
        left = self.helper(root.left)
        right = self.helper(root.right)
        if left == 0 or right == 0:
            self.count += 1
            return 1
        if left == 1 or right == 1:
            return 2
        else:
            return 0

    def minCameraCover(self, root: TreeNode) -> int:
        self.count = 0
        return (self.helper(root) == 0) + self.count
