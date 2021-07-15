# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.node = None
    def findtarget(self,org,clone,target):
        
        if not org or not clone:
            return None
        
        
        if org.val==target.val==clone.val:
            #self.node = clone
            return clone
        return self.findtarget(org.left,clone.left,target) or self.findtarget(org.right,clone.right,target)
        
        
        
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        
        return self.findtarget(original,cloned,target)
        #return self.node

