# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        #DFS
        stack = [(root, [])]
        maxDiff = 0
        while stack:
            node, anc = stack.pop()
            if anc:
                maxDiff = max(maxDiff, 
                         max(abs(node.val - v) for v in anc))
            if node.left:
                stack.append((node.left, anc + [node.val]))
            if node.right:
                stack.append((node.right, anc + [node.val]))
        return maxDiff
