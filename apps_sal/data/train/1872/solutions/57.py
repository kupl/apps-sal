# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        if root == None:
            return 0
        traversing = [(1, root)]
        level_sum = dict()
        while traversing:
            cur = traversing.pop()
            level_sum[cur[0]] = level_sum.get(cur[0], 0) + cur[1].val
            if cur[1].left:
                traversing.append((cur[0] + 1, cur[1].left))
            if cur[1].right:
                traversing.append((cur[0] + 1, cur[1].right))
        return max((v, k) for k, v in level_sum.items())[1]
