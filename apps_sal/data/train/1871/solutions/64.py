class Solution:

    def maxAncestorDiff(self, root: TreeNode) -> int:

        def traverse(root, anc, diff):
            if root:
                for an in anc:
                    if abs(root.val - an) > diff:
                        diff = abs(root.val - an)
                diff = traverse(root.left, anc + [root.val], diff)
                diff = traverse(root.right, anc + [root.val], diff)
            return diff
        return traverse(root, [], 0)
