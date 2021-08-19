class Solution:

    def deepestLeavesSum(self, root: TreeNode) -> int:
        q = [root]
        while q:
            (pre, q) = (q, [child for p in q for child in [p.left, p.right] if child])
        return sum((node.val for node in pre))
