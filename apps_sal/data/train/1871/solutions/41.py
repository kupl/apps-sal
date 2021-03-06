class Solution:
    maxDiff = 0

    def maxAncestorDiff(self, root: TreeNode) -> int:
        if not root:
            return 0
        currPath = []

        def dfs(currNode, currPath):
            currPath.append(currNode.val)
            if currNode.left:
                dfs(currNode.left, currPath)
            if currNode.right:
                dfs(currNode.right, currPath)
            self.maxDiff = max(self.maxDiff, max(currPath) - min(currPath))
            currPath.pop()
        dfs(root, currPath)
        return self.maxDiff
