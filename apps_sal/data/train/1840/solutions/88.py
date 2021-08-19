class Solution:

    def __init__(self):
        self.max_cnt = 0

    def longestZigZag(self, root: TreeNode) -> int:
        self.helper(root, True, 0)
        self.helper(root, False, 0)
        return self.max_cnt

    def helper(self, root, isLeft, cnt):
        if root is None:
            return
        if isLeft:
            self.helper(root.left, False, cnt + 1)
            self.helper(root.right, True, 1)
        else:
            self.helper(root.right, True, cnt + 1)
            self.helper(root.left, False, 1)
        self.max_cnt = max(self.max_cnt, cnt)
