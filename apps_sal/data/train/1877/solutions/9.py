class Solution:

    def sufficientSubset(self, root: TreeNode, limit: int) -> TreeNode:
        if not root:
            return root

        def dfs(node, value):
            if not node:
                return False
            value += node.val
            lret = dfs(node.left, value)
            rret = dfs(node.right, value)
            if not node.left and (not node.right):
                if value < limit:
                    return False
                return True
            if not lret:
                node.left = None
            if not rret:
                node.right = None
            if lret or rret:
                return True
            return False
        res = dfs(root, 0)
        if res:
            return root
