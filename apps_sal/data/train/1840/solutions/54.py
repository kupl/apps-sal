# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
_max = 0
class Solution:
    def preorder(self,root, lr, cur_len):
        nonlocal _max
        
        if(root==None):
            return
        
        _max = max(_max,cur_len)
        
        if(lr=='l'):
            self.preorder(root.left,'l',1)
            self.preorder(root.right,'r',cur_len+1)
        elif(lr=='r'):
            self.preorder(root.left,'l',cur_len+1)
            self.preorder(root.right,'r',1)
        else:
            self.preorder(root.left,'l',cur_len+1)
            self.preorder(root.right,'r',cur_len+1)

            
        
    def longestZigZag(self, root: TreeNode) -> int:
        nonlocal _max
        _max = 0
        self.preorder(root,None,0)
        
        return _max

