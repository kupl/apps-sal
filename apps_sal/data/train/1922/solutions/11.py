# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        ans = 0
        def recursive(root):
            nonlocal ans
            if not root.left and not root.right:
                return 0, 0
            left_cover = 1
            right_cover= 1
            left_camera = 0
            right_camera  = 0
            if root.left:
                left_cover, left_camera = recursive(root.left)
            if root.right:
                right_cover, right_camera = recursive(root.right)
            if not (left_cover and right_cover):
                ans +=1
                return 1, 1
            elif left_camera or right_camera:
                return 1, 0
            else:
                return 0, 0
        return ans if recursive(root)[0] else ans+1
                

