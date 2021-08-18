class Solution:
    def sufficientSubset(self, root: TreeNode, limit: int) -> TreeNode:
        def dfs(node, value):
            if not node:
                return False
            value += node.val
            l_side = dfs(node.left, value)
            r_side = dfs(node.right, value)
            if not node.left and not node.right:
                if value < limit:
                    return False
                return True
            if not l_side:
                node.left = None
            if not r_side:
                node.right = None
            if l_side or r_side:
                return True
            return False
        if dfs(root, 0):
            return root
        return
