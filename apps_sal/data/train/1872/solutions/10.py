
from collections import defaultdict


class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
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
