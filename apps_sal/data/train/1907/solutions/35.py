class Solution:

    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:

        def dfs(original, cloned, target):
            if not original:
                return None
            if original == target:
                return cloned
            left = dfs(original.left, cloned.left, target)
            right = dfs(original.right, cloned.right, target)
            if left:
                return left
            else:
                return right
        result = dfs(original, cloned, target)
        return result
