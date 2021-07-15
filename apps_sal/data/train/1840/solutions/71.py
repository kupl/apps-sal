# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        self.max_ = 0
        def preorder(root,count,dir_):
            self.max_ = max(self.max_,count)
            
            if root.left:
                if dir_ == 1 or dir_==-1:
                    preorder(root.left,count+1,0)
                else:
                    preorder(root.left,1,0)
                    
            if root.right:
                if dir_ == 0 or dir_==-1:
                    preorder(root.right,count+1,1)
                else:
                    preorder(root.right,1,1)
                    
        preorder(root,0,-1)
        return self.max_
            

