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

            row = new_row

        return rv
