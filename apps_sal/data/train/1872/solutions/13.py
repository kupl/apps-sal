class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        self.max_sum = {}

        def sum_tree(node: TreeNode, level):

            if not node:
                return
            sum_tree(node.left, level + 1)
            sum_tree(node.right, level + 1)
            if level in self.max_sum:
                self.max_sum[level] += node.val
            else:
                self.max_sum[level] = node.val

        sum_tree(root, 1)
        output, max_val = float('inf'), -float('inf')
        for key, val in list(self.max_sum.items()):
            if val > max_val:
                output, max_val = key, val
            elif val == max_val:
                output = min(key, output)
        return output
