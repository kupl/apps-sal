class Solution:

    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        self.res = None

        def dfs(node, target):
            if self.res:
                return
            if not node:
                return
            if node.val == target.val:
                self.res = node
            dfs(node.left, target)
            dfs(node.right, target)
        dfs(cloned, target)
        return self.res
