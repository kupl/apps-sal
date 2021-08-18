
class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:

        def dfs(root, target):
            if root and root.val == target:
                return root
            if root:
                return dfs(root.left, target) or dfs(root.right, target)

        return dfs(cloned, target.val)
