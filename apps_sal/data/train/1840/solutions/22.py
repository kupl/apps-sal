class Solution:

    def longestZigZag(self, root: TreeNode) -> int:

        def aux(root):
            if not root:
                return [-1, -1, -1]
            left = aux(root.left)
            right = aux(root.right)
            ans = max(max(left[1], right[0]) + 1, left[2], right[2])
            return [left[1] + 1, right[0] + 1, ans]
        return aux(root)[2]
