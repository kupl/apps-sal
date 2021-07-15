# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(r, val = float('-inf')):
            if r:
                ans = 1 if r.val >= val else 0
                new_val = max(r.val, val)
                ans += dfs(r.left, new_val)
                ans += dfs(r.right, new_val)
                return ans
            return 0
        return dfs(root)
