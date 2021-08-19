# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:

        row = [root]
        max_sum = root.val
        rv = row_count = 1

        while any(row):
            new_row = []
            row_sum = 0

            for node in row:
                for child in (node.left, node.right):
                    if child:
                        new_row.append(child)
                        row_sum += child.val

            if new_row:
                row_count += 1

            if row_sum > max_sum:
                max_sum = row_sum
                rv = row_count

            #max_sum = max(max_sum, row_sum)
            row = new_row

        return rv
