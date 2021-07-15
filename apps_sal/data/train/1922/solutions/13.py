# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        
        @lru_cache(None)
        def cal(root, st):
            if root:
                if st == 1:
                    return min(cal(root.left, 2)+cal(root.right, 2),
                              1 + cal(root.left, 1) + cal(root.right, 1))
                elif st == 2:
                    if root.left == root.right == None:
                        return 1
                    if root.left and root.right:                        
                        return min(cal(root.left, 3)+cal(root.right, 2),
                                    cal(root.left, 2)+cal(root.right, 3),
                                    1 + cal(root.left, 1) + cal(root.right, 1))
                    else:
                         return min(cal(root.left, 3)+cal(root.right, 3),
                                    cal(root.left, 3)+cal(root.right, 3),
                                    1 + cal(root.left, 1) + cal(root.right, 1))
                        
                elif st == 3:
                    return 1 + cal(root.left, 1) + cal(root.right, 1)
            else:
                return 0
            
        return cal(root, 2)
