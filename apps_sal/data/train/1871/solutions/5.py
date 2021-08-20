class Solution:

    def maxAncestorDiff(self, root: TreeNode) -> int:
        return self.helper(root, [], 0)

    def helper(self, root, anc, prevmax):
        if root == None:
            return prevmax
        real_prev = prevmax
        for a in anc:
            prevmax = max(prevmax, abs(a - root.val))
        anc.append(root.val)
        real_anc = list(anc)
        left = self.helper(root.left, anc, prevmax)
        right = self.helper(root.right, real_anc, prevmax)
        return max(left, right)
