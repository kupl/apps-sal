# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        if not root: return 0
        
        queue = [root]
        maxLevel = level = 1
        maxSum = root.val
        
        while queue:
            nextLevel = []
            s = 0
            for n in queue:
                s += n.val
                if n.left:
                    nextLevel.append(n.left)
                if n.right:
                    nextLevel.append(n.right)
            if s > maxSum:
                maxSum, maxLevel = s, level
            queue = nextLevel
            level += 1
        return maxLevel
