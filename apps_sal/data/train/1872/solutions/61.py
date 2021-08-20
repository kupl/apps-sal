class Solution:

    def maxLevelSum(self, root: TreeNode) -> int:
        res = self.helper(root)
        return res.index(max(res)) + 1

    def helper(self, root):
        if not root:
            return []
        (left, right) = (self.helper(root.left), self.helper(root.right))
        l = min(len(left), len(right))
        res = [root.val] + [sum(p) for p in zip(left, right)] + left[l:] + right[l:]
        return res
