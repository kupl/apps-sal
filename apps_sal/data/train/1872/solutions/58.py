# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelSumHelper(self, node, level, sums):
        if node is None:
            return sums
        if(len(sums) == level):
            sums.append(node.val)
        else:
            sums[level] += node.val
        sums = self.levelSumHelper(node.left, level + 1, sums)
        sums = self.levelSumHelper(node.right, level + 1, sums)
        return sums

    def maxLevelSum(self, root: TreeNode) -> int:
        sums = self.levelSumHelper(root, 0, [])
        # print(sums)
        m = sums[0]
        ret = 0
        for i, s in enumerate(sums):
            # print(i,s)
            #print(m, ret)
            if s > m:
                m = s
                ret = i
        return ret + 1
