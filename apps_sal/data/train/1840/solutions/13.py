# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        if root == None:
            return 0
        maxZigZag = 0
        def zigZagStart(root):##direction will correspond to -1 for left and 1 for right
            nonlocal maxZigZag
            if root == None or (root.left == None and root.right == None):
                return [0,0]
            ll,lr = zigZagStart(root.left)
            rl,rr = zigZagStart(root.right)
            bestLeft = 0
            bestRight = 0
            if root.left:
                bestLeft = 1+lr
            if root.right:
                bestRight = 1+rl
            maxZigZag = max(maxZigZag,bestLeft,bestRight)
            return [bestLeft,bestRight]
        zigZagStart(root)
        return maxZigZag
