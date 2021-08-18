class Solution:
    def __init__(self):
        self.sums = []
        self.current_level = 1

    def helper(self, root):
        if root is None:
            return
        if len(self.sums) < self.current_level:
            self.sums.append(root.val)
        else:
            self.sums[self.current_level - 1] += root.val
        self.current_level += 1
        self.helper(root.left)
        self.helper(root.right)
        self.current_level -= 1

    def maxLevelSum(self, root: TreeNode) -> int:
        self.helper(root)
        return self.sums.index(max(self.sums)) + 1
