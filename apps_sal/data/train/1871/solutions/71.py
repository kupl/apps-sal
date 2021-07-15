# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.max_diff = -1
    
    def maxAncestorDiff(self, root: TreeNode) -> int:
        
        def max_diff_calc(root):
            if not root:
                return []
            ancestors = max_diff_calc(root.left)
            ancestors.extend(max_diff_calc(root.right))
            for ans in ancestors:
                if abs(root.val - ans) > self.max_diff:
                    self.max_diff = abs(root.val - ans)
            ancestors.append(root.val)
            return ancestors
        
        max_diff_calc(root)
        return self.max_diff
