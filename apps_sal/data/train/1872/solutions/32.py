# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        curr = [root]
        currLevel = 0
        res = 0
        resSum = float(\"-inf\")

        while curr:
            currSum = 0
            currLevel+=1
            nexx = []
            for n in curr:
                currSum += n.val
                if n.left:
                    nexx.append(n.left)
                if n.right:
                    nexx.append(n.right)
            if resSum < currSum:
                res = currLevel
                resSum = currSum
            curr = nexx
        
        return res
