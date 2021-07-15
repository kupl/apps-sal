# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper_rec(self,root,tempMax):
        if root is None:
            return
        
        if root.val >= tempMax:
            self.count += 1
            tempMax=max(root.val,tempMax)
        self.helper_rec(root.left,tempMax)
        self.helper_rec(root.right, tempMax)

    def goodNodes(self, root: TreeNode) -> int:
        if root is None:
            return 0
        #self.tempMax=0
        self.count=0
        self.helper_rec(root,root.val)
        return self.count
