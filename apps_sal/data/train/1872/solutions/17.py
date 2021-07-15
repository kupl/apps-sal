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

        nodes = [(1, root)]
        maxlevelsum = -float('inf')-1
        maxlevel = 0
        currlevel = 1
        currlevelsum = 0
        while len(nodes) != 0:
            curr = nodes.pop(0)
            if curr[0] == currlevel:
                currlevelsum += curr[1].val
            else:
                if currlevelsum > maxlevelsum:
                    maxlevelsum = currlevelsum
                    maxlevel = currlevel
                currlevel = curr[0]
                currlevelsum = curr[1].val

            if curr[1].left is not None:
                nodes.append((curr[0] + 1, curr[1].left))
            if curr[1].right is not None:
                nodes.append((curr[0] + 1, curr[1].right))
            if len(nodes) == 0:
                if currlevelsum > maxlevelsum:
                    maxlevelsum = currlevelsum
                    maxlevel = currlevel

        return maxlevel
