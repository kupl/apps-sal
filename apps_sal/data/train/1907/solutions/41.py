# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:

        def recur(orig, clon):
            if (orig and not clon) or (clon and not orig):
                return False
            if not orig and not clon:
                return True

            if orig.val != clon.val:
                return False
            left = recur(orig.left, clon.left)
            right = recur(orig.right, clon.right)
            return left and right

        ans = None

        def dfs(original, cloned, target):
            nonlocal ans
            if original == target:
                isSame = recur(target, cloned)
                if isSame:
                    ans = cloned
                    return
            if original.left:
                dfs(original.left, cloned.left, target)
            if original.right:
                dfs(original.right, cloned.right, target)

        dfs(original, cloned, target)
        return ans
