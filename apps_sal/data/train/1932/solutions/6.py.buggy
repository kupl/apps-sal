# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def btreeGameWinningMove(self, root, n, x):
        \"\"\"
        :type root: TreeNode
        :type n: int
        :type x: int
        :rtype: bool
        \"\"\"
        self.l, self.r = None, None
        def numNodes(root):
            if not root:
                return 0 
            l = numNodes(root.left)
            r = numNodes(root.right)
            if root.val == x:
                self.l = l
                self.r = r
            return l+r+1
        
        numNodes(root)
        max_score = max(self.l, self.r, n-self.l-self.r-1)
        
        return max_score > n/2
