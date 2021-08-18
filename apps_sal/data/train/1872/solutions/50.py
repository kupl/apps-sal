
class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:

        from collections import defaultdict

        self.sums = defaultdict(int)

        def helper(node, level):
            if node is not None:
                self.sums[level] += node.val
                helper(node.right, level + 1)
                helper(node.left, level + 1)

        helper(root, 1)

        return sorted(list(self.sums.items()), key=lambda t: t[1], reverse=True)[0][0]
