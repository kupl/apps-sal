# Definition for a binary tree node.\r
# class TreeNode:\r
#     def __init__(self, val=0, left=None, right=None):\r
#         self.val = val\r
#         self.left = left\r
#         self.right = right\r
class Solution:\r
    def deepestLeavesSum(self, root: TreeNode) -> int:\r
        currentLevel = [root]\r
        while currentLevel:\r
            currentSum = 0\r
            nextLevel = []\r
            for node in currentLevel:\r
                currentSum += node.val\r
                if node.left:\r
                    nextLevel.append(node.left)\r
                if node.right:\r
                    nextLevel.append(node.right)\r
            currentLevel = nextLevel\r
        return currentSum
