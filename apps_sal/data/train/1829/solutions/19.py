class Solution:

    def goodNodes(self, root: TreeNode) -> int:
        count = 0

        def dfs(node, prevVal):
            nonlocal count
            if node:
                maxPrev = max(node.val, prevVal)
                if node.val >= prevVal:
                    count += 1
                dfs(node.left, maxPrev)
                dfs(node.right, maxPrev)
        dfs(root, root.val)
        return count
