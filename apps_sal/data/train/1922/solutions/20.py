# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        
        
        def dfs(node):
            nonlocal cnt
            
            if node:
                left = dfs(node.left)
                right = dfs(node.right)
                
                if not left or not right:
                    cnt += 1
                    return 2
                elif left == 2 or right == 2:
                    return 1
                else:
                    return 0
            else:
                return 1
        
        cnt = 0
        
        if not dfs(root):
            return cnt + 1
        else:
            return cnt
        
        
        

