class Solution:

    def maxLevelSum(self, root: TreeNode) -> int:
        res = self.helper(root)
        return res.index(max(res)) + 1

    def helper(self, root):
        if not root:
            return []
        (res, left, right) = ([root.val], self.helper(root.left), self.helper(root.right))
        l = min(len(left), len(right))
        for i in range(l):
            res.append(left[i] + right[i])
        res = res + left[l:] + right[l:]
        return res
