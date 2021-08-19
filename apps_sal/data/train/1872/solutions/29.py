# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        if root is None:
            return 0

        queue = [root]
        res = 0
        result = []
        while len(queue) != 0:
            l = len(queue)
            sum1 = 0
            for i in range(l):
                item = queue.pop(0)
                sum1 += item.val
                if item.left != None:
                    queue.append(item.left)
                if item.right != None:
                    queue.append(item.right)
            result.append(sum1)
        return result.index(max(result)) + 1
