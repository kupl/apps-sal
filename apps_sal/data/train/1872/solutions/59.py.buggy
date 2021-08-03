# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        
        self.l = [0]*100000
        self.max = float(\"-inf\")
        self.ans = 0
        
        def ankit(root,level):
            
            if(root is not None):
                ankit(root.left,level+1)
                self.l[level]+= root.val
                ankit(root.right,level+1)
                
        ankit(root,1)
        return self.l.index(max(self.l))
                    
                
            
        
