class Solution:

    def maxLevelSum(self, root: TreeNode) -> int:
        collector = collections.defaultdict(int)

        def helper(root, d):
            if not root:
                return
            collector[d] += root.val
            helper(root.right, d + 1)
            helper(root.left, d + 1)
            return
        helper(root, 0)
        print(collector)
        best = 0
        for (k, v) in list(collector.items()):
            if v > collector[best]:
                best = k
        return best + 1
