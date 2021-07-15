# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        if len(preorder) == 1:
            return root
        # left = [i for i in preorder if i < root.val]
        # right = [i for i in preorder if i > root.val]
        ind = len(preorder)
        for i, j in enumerate(preorder):
            if j > root.val:
                ind = i
                break
        root.left = self.bstFromPreorder(preorder[1:ind])
        root.right = self.bstFromPreorder(preorder[ind:])
        
        return root
