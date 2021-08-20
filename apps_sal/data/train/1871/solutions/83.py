class Solution:

    def maxAncestorDiff(self, root: TreeNode) -> int:
        self.mx = 0

        def dfs(node, visited):
            if node is None:
                return
            else:
                for v in visited:
                    if abs(v - node.val) > self.mx:
                        self.mx = abs(v - node.val)
            dfs(node.left, visited + [node.val])
            dfs(node.right, visited + [node.val])
            return
        dfs(root, [])
        return self.mx
