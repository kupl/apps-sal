class Solution:

    def goodNodes(self, root: TreeNode) -> int:

        def helper(root, max_val):
            if not root:
                return 0
            ans = 0
            if root.val >= max_val:
                max_val = root.val
                ans += 1
            return ans + helper(root.left, max_val) + helper(root.right, max_val)
        return helper(root, -float('inf'))
