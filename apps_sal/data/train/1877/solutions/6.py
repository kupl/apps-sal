class Solution:

    def check_limit(self, root, limit):
        if not root:
            return float('-inf')
        left_sum = self.check_limit(root.left, limit - root.val)
        right_sum = self.check_limit(root.right, limit - root.val)
        if left_sum != float('-inf') and left_sum + root.val < limit:
            root.left = None
        if right_sum != float('-inf') and right_sum + root.val < limit:
            root.right = None
        max_ = max(left_sum, right_sum)
        if max_ == float('-inf'):
            return root.val
        return max_ + root.val

    def sufficientSubset(self, root: TreeNode, limit: int) -> TreeNode:
        if (self.check_limit(root, limit) or 0) < limit:
            return None
        else:
            return root
