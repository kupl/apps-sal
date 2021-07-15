# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.ans = 0
        def tra(node, maxtillnow):
            if node:
                if node.val>=maxtillnow:
                    self.ans +=1
                tra(node.left, max(maxtillnow, node.val))
                tra(node.right, max(maxtillnow, node.val))
            
            
        tra(root, float('-inf'))
        
        return self.ans
