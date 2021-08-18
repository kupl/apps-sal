class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        return self.helper(root)[1]

    def helper(self, root):
        if root == None:
            return (None, 0, None)
        elif root.left == None and root.right == None:
            return (root.val, 0, root.val)
        elif root.left == None:
            (r_low, r_long, r_high) = self.helper(root.right)
            return (min(r_low, root.val), max(r_long, abs(root.val - r_low), abs(root.val - r_high)), max(r_high, root.val))
        elif root.right == None:
            (l_low, l_long, l_high) = self.helper(root.left)
            return (min(l_low, root.val), max(l_long, abs(root.val - l_low), abs(root.val - l_high)), max(l_high, root.val))
        else:
            (r_low, r_long, r_high) = self.helper(root.right)
            (l_low, l_long, l_high) = self.helper(root.left)
            print(root, r_high, l_high, l_long, r_long)
            return (min(l_low, root.val, r_low), max(r_long, l_long, abs(root.val - min(l_low, r_low)), abs(root.val - max(r_high, l_high))), max(r_high, l_high, root.val))
