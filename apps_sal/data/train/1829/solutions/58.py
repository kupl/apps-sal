class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(r, val=float('-inf')):
            if r:
                ans = 1 if r.val >= val else 0
                new_val = max(r.val, val)
                ans += dfs(r.left, new_val)
                ans += dfs(r.right, new_val)
                return ans
            return 0
        return dfs(root)
