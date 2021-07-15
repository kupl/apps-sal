# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        def original_clone(original,cloned,target):
            nonlocal a;
            if original==None:
                return 
            if original.val==target.val:
                a=cloned
                return 
            original_clone(original.left,cloned.left,target)
            original_clone(original.right,cloned.right,target)
        a=None
        original_clone(original,cloned,target)
        return a
        

