class Solution:

    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:

        def match(original, copy):
            if not original:
                return None
            if original == target:
                return copy
            return match(original.left, copy.left) or match(original.right, copy.right)
        return match(original, cloned)
