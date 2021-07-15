# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        def helper(root, level, sums):
            if not root: return
            if level > len(sums):
                sums.append(0)
            sums[level-1] += root.val
            helper(root.left, level+1, sums)
            helper(root.right, level+1, sums)
            
        sums = []
        helper(root, 1, sums)
        m, ix = -float('inf'), -1
        for i in range(len(sums)):
            if sums[i] > m:
                m, ix= sums[i], i
        return ix +1
