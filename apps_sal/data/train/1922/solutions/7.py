# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        # three cases for a node (root), DP: up -> bottom
        # 0: root is not covered, all nodes below are covered
        # 1: root is covered, all nodes below are covered, root has no camera
        # 2: root is covered, all nodes below are covered, root has a camera
        
        # 0: L, R children both in case 1
        # 1: L, R can be 1 or 2, at least one child is in case 2
        # 2: L, R children can be any case
        
        def dp(node):
            if not node:
                return [0, 0, float(inf)]
            
            L = dp(node.left)
            R = dp(node.right)
            dp0 = L[1] + R[1]
            dp1 = min(L[2] + min(R[1:]), min(L[1:]) + R[2])
            dp2 = 1 + min(L) + min(R)
            return [dp0, dp1, dp2]
        return min(dp(root)[1:])
            

