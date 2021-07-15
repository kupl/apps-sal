# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        queue = [root]
        curLevel = maxLevel = 1
        output = root.val
        
        while queue:
            s, nextLevel = 0, []
            for n in queue:
                if n.left:
                    nextLevel.append(n.left)
                if n.right:
                    nextLevel.append(n.right)
                s += n.val
            if s > output:
                output = s
                maxLevel = curLevel
            curLevel += 1
            queue = nextLevel
        return maxLevel

