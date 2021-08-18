class Solution:
    def sufficientSubset(self, root: TreeNode, limit: int) -> TreeNode:

        def dfs(node, value):
            if not node:
                return False
            value += node.val
            l = dfs(node.left, value)
            r = dfs(node.right, value)
            if not node.left and not node.right:
                if value < limit:
                    return False
                return True
            if not l:
                node.left = None
            if not r:
                node.right = None
            if l or r:
                return True
            return False
        res = dfs(root, 0)
        if res:
            return root
        return
