# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorder(self, root, max_so_far, ctr):
        if not root:
            return
        if root.val>=max_so_far:
            max_so_far = root.val
            ctr[0] += 1
        self.preorder(root.left, max_so_far, ctr)
        self.preorder(root.right, max_so_far, ctr)
        
    def goodNodes(self, root: TreeNode) -> int:
        max_so_far = -111111111111111
        ctr = [0]
        self.preorder(root, max_so_far, ctr)
        return ctr[0]
        

