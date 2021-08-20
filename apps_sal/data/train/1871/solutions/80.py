class Solution:
    abs_max = -99999

    def construct_all_pairs(self, subtree):
        if subtree is None:
            return []
        else:
            lp = self.construct_all_pairs(subtree.left)
            rp = self.construct_all_pairs(subtree.right)
            for l in lp:
                if abs(subtree.val - l) > self.abs_max:
                    self.abs_max = abs(subtree.val - l)
            for r in rp:
                if abs(subtree.val - r) > self.abs_max:
                    self.abs_max = abs(subtree.val - r)
            return [subtree.val] + lp + rp

    def maxAncestorDiff(self, root: TreeNode) -> int:
        self.construct_all_pairs(root)
        return self.abs_max
