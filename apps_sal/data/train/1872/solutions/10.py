# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import defaultdict


class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        # have a rst that saves sum at each level
        rstDict = dict()

        def maxLevelRec(root, level):
            nonlocal rstDict
            if(not root):
                return
            if(level in rstDict):
                rstDict[level] += root.val
            else:
                rstDict[level] = root.val
            maxLevelRec(root.left, level + 1)
            maxLevelRec(root.right, level + 1)
        maxLevelRec(root, 1)
        maxSum = max(rstDict.values())
        for key in list(rstDict.keys()):
            if(rstDict[key] == maxSum):
                return key
