class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        if not root:
            return 0

        def maxDiff(root: TreeNode, ancestors: List[int]) -> int:
            if not root:
                return 0

            left_max = maxDiff(root.left, ancestors + [root.val])
            right_max = maxDiff(root.right, ancestors + [root.val])
            diffs = [abs(ancestor - root.val) for ancestor in ancestors]
            return max(diffs + [left_max, right_max])

        return maxDiff(root, [])
