class Solution:

    def goodNodes(self, root: TreeNode) -> int:
        stack = []
        ans = [0]

        def dfs(root):
            if not stack or root.val >= stack[-1].val:
                stack.append(root)
                ans[0] += 1
            if root.left:
                dfs(root.left)
            if root.right:
                dfs(root.right)
            if stack and root == stack[-1]:
                stack.pop()
        dfs(root)
        return ans[0]
