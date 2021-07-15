# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        
        if len(preorder) == 0:
            return None
        
        return self.helper(preorder,0,len(preorder))
        
    def helper(self,preorder,start,end):
        # print(start,end,preorder[start:end])
        if start >= end:
            return None
        
        split = start + 1
        root = TreeNode(preorder[start])
        
        while split < end and preorder[start] > preorder[split]:
            split+=1
        
        root.left = self.helper(preorder,start + 1,split)
        root.right = self.helper(preorder,split,end)
        return root
