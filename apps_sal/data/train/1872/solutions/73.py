# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:

        level_sums = [[root.val]]

        q = [root]

        while q:
            temp = []
            for _ in range(len(q)):

                node = q.pop(0)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

                temp.append(node.val)

            level_sums.append(temp)

        sums = [sum(l) for l in level_sums]

        return sums.index(max(sums))
