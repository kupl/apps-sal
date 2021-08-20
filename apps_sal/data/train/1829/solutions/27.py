class Solution:

    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0

        def helper(root, maxVal):
            if root is None:
                return
            if root.val >= maxVal:
                maxVal = root.val
                self.count += 1
            helper(root.left, maxVal)
            helper(root.right, maxVal)
        helper(root, -10001)
        return self.count
