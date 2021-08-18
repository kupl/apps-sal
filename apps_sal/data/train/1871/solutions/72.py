class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:

        res = 0
        if not root:
            return

        def dfs(node, a):
            nonlocal res
            tmp = max(abs(x - node.val) for x in a) if a else 0
            res = max(res, tmp)
            if node.left:
                a.append(node.left.val)
                dfs(node.left, a)
                a.pop()
            if node.right:
                a.append(node.right.val)
                dfs(node.right, a)
                a.pop()
            return

        dfs(root, [root.val])
        return res
