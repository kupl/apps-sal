class Solution:
    answer = 0

    def maxAncestorDiff(self, root: TreeNode) -> int:
        def dfs(node, max_v, min_v):
            self.answer = max(self.answer, abs(max_v - node.val))
            self.answer = max(self.answer, abs(min_v - node.val))

            if node.left:
                dfs(node.left, max(max_v, node.val), min(min_v, node.val))
            if node.right:
                dfs(node.right, max(max_v, node.val), min(min_v, node.val))

        dfs(root, root.val, root.val)
        return self.answer
